
#undef Error_Handler
#undef Error_Handler()
#define STM32_G
#define HAL_FDCAN_MODULE_ENABLED

#include <functional>

#if defined(STM32G474xx) || defined(STM32_G)
#include "stm32g4xx_hal.h"
// TODO: rework this dependency
#if __has_include("utils.h")
#include "utils.h"
#else
#define CRITICAL_SECTION(code) code
#endif
#else
#define CRITICAL_SECTION(code) code
#include <unistd.h>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <stdint.h>
#endif

// timestamp conversion macros
#define SEC_TO_US(sec) ((sec) * 1000000)
#define NS_TO_US(ns) ((ns) / 1000)

#ifdef __linux__
uint64_t _micros_64();
#endif

struct UtilityConfig {
    const std::function<uint64_t()> micros_64;
    const std::function<void()> error_handler;

    explicit UtilityConfig(std::function<uint64_t()>&& micros, std::function<void()>&& handler):
        micros_64(micros),
        error_handler(handler)
    {};
};

#ifdef __linux__
extern UtilityConfig DEFAULT_CONFIG;
#endif

template <typename T>
class IListener {
public:
    virtual void accept(T) = 0;
};
#include <tuple>
#include <type_traits>

#include "libcanard/canard.h"

class AbstractAllocator {
protected:
    UtilityConfig& utilities;
public:
    AbstractAllocator(size_t size, UtilityConfig& utilities): utilities(utilities) {};
    virtual void* allocate(CanardInstance* ins, size_t amount) = 0;
    virtual void free(CanardInstance* ins, void* pointer) = 0;
    virtual ~AbstractAllocator() {}
};

#include "o1heap/o1heap.h"


class O1Allocator : public AbstractAllocator {
private:
    O1HeapInstance* o1heap;
    void* memory_arena;
    void align_self(size_t size);
    bool is_self_allocated = false;
public:
    O1Allocator(size_t size, void* memory,  UtilityConfig& utilities);
    explicit O1Allocator(size_t size, UtilityConfig& utilities);
    ~O1Allocator();

    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;
};


class SystemAllocator : public AbstractAllocator {
public:
	// TODO: do something with size value?
	explicit SystemAllocator(size_t size, UtilityConfig& utilities): AbstractAllocator(size, utilities) {};
    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;
};

#include <cstdint>

extern const uint32_t CanardFDCANLengthToDLC[65];
extern size_t fdcan_dlc_to_len(uint32_t);

#include <memory>
#include <functional>
#ifdef __linux__
#include <iostream>
#endif

#include "libcanard/canard.h"

extern std::unique_ptr<AbstractAllocator> _alloc_ptr;

inline void* alloc_f (CanardInstance* ins, size_t amount) {
    if (!_alloc_ptr) {
        #ifdef __linux__
        std::cerr << "Tried to allocate canard memory before creating provider&allocator!" << std::endl;
        #endif
        exit(1);
    }
    return _alloc_ptr->allocate(ins, amount);
}
inline void free_f (CanardInstance* ins, void* pointer) {
    if (!_alloc_ptr) {
        #ifdef __linux__
        std::cerr << "Tried to free (?) canard memory before creating provider&allocator!" << std::endl;
        #endif
        exit(1);
    }
    return _alloc_ptr->free(ins, pointer);
}

class AbstractCANProvider {
    friend class CyphalInterface;

protected:
    const size_t CANARD_MTU;
    const size_t WIRE_MTU;
    CanardTxQueue queue;
    CanardInstance canard;
    UtilityConfig& utilities;

    AbstractCANProvider() = delete;
    AbstractCANProvider(size_t canard_mtu, size_t wire_mtu, UtilityConfig& utilities) : AbstractCANProvider(canard_mtu, wire_mtu, 200, utilities) {};
    AbstractCANProvider(size_t canard_mtu, size_t wire_mtu, size_t queue_len, UtilityConfig& utilities) :
        WIRE_MTU(wire_mtu),
        CANARD_MTU(canard_mtu),
        queue(canardTxInit(queue_len, CANARD_MTU)),
        utilities(utilities)
    {};

    template <class T>
    void setup(T* ptr, CanardNodeID node_id) {
        using namespace std::placeholders;

        if (_alloc_ptr) {
#ifdef __linux__
            std::cerr << "Tried to call setup in provider twice!" << std::endl;
#endif
            utilities.error_handler();
        }
        _alloc_ptr = std::unique_ptr<T>(ptr);

        canard = canardInit(alloc_f, free_f);
        canard.node_id = node_id;
    }
public:
    typedef void Handler;

    virtual uint32_t len_to_dlc(size_t len) = 0;
    virtual size_t dlc_to_len(uint32_t dlc) = 0;
    virtual void can_loop() = 0;
    virtual bool read_frame(CanardFrame*)  = 0;
    virtual int write_frame(const CanardTxQueueItem* ti) = 0;
    void process_canard_rx(CanardFrame*);
    void process_canard_tx();

    virtual ~AbstractCANProvider();
};

// Time to transmit one frame + delay for 25ns bit time ~ (25*29 (ext id) + 25*64 (body)) * 1.5
#define ONE_FULL_FRAME_T 2620
// Cycles = ONE_FULL_FRAME_T / 200 * 32
#define ONE_FULL_FRAME_CYCLES 420

// 32 cycles ~~ 200 ns delay for 160Mhz core clock
__attribute__((optimize("O1"))) static inline void delay_cycles(uint16_t cycles = 32) {
    /* Reference: https://developer.arm.com/documentation/ddi0439/b/Programmers-Model/Instruction-set-summary/Cortex-M4-instructions?lang=en
     *
     * // 6 тактов на (cycles - 8) / 5
       sub     r3, r0, #5         // 1 такт
       ldr     r2, .L6            // 2 такта
       smull   r1, r2, r3, r2     // 1 такт
       asr     r3, r3, #31        // 1 такт
       rsb     r3, r3, r2, asr #1 // 1 такт
     *
     * // 2 такта на стартовую проверку
       ands    r3, r3, #255       // 1 такт
       bxeq    lr                 // 1 такт ("Conditional branch completes in a single cycle if the branch is not taken.")
     *
     * // ~5 тактов на цикл
       .L3:
       nop                       // 1 такт
       sub     r3, r3, #1        // 1 такт
       ands    r3, r3, #255      // 1 такт
       bne     .L3               // 1 + 1-3 такта, в среднем 2(3?)
     *
     * Всего 5 тактов на цикл + 8 в начале.
     */

    uint8_t real_cycles = (cycles - 8) / 5;
    while (real_cycles--) {
        __asm__("nop");
    }
}
#if (defined(STM32G474xx) || defined(STM32_G)) && defined(HAL_FDCAN_MODULE_ENABLED)


class G4CAN : public AbstractCANProvider {
public:
    typedef FDCAN_HandleTypeDef* Handler;
private:
    FDCAN_HandleTypeDef* handler;
    G4CAN(Handler handler, size_t queue_len, UtilityConfig& utilities):
        AbstractCANProvider(CANARD_MTU_CAN_FD, 72, queue_len, utilities), handler(handler) {};
public:
    
    template <class T, class... Args> static G4CAN* create_bss(
        std::byte** inout_buffer,
        Handler handler,
        CanardNodeID node_id,
        size_t queue_len,
        Args&&... args,
        UtilityConfig& utilities
    ) {
        std::byte* allocator_loc = *inout_buffer;
        auto allocator_ptr = new (allocator_loc) T(queue_len * sizeof(CanardTxQueueItem) * 2.5, args..., utilities);
    
        std::byte* provider_loc = allocator_loc + sizeof(T);
        auto ptr = new (provider_loc) G4CAN(handler, queue_len, utilities);
    
        ptr->setup<T>(allocator_ptr, node_id);

        *inout_buffer = provider_loc + sizeof(G4CAN);
        return ptr;
    }

    template <class T, class... Args> static G4CAN* create_heap(
        Handler handler,
        CanardNodeID node_id,
        size_t queue_len,
        Args&&... args,
        UtilityConfig& utilities
    ) {
        auto allocator_ptr = new T(queue_len * sizeof(CanardTxQueueItem) * 2.5, args..., utilities);
        auto ptr = new G4CAN(handler, queue_len, utilities);
        ptr->setup<T>(allocator_ptr, node_id);

        return ptr;
    }

    uint32_t len_to_dlc(size_t len) override;
    size_t dlc_to_len(uint32_t dlc) override;
    void can_loop() override;
    bool read_frame(CanardFrame*)  override;
    int write_frame(const CanardTxQueueItem* ti) override;
};

#endif

#include <memory>


#define DEFAULT_TIMEOUT_MICROS 1000000 // 1 sec

template <typename ObjType>
using cyphal_serializer = int8_t (*)(const ObjType* const, uint8_t* const, size_t* const);
template <typename ObjType>
using cyphal_deserializer = int8_t (*)(ObjType* const, const uint8_t*, size_t* const);

#define TYPE_ALIAS(ALIAS_NAME, T)                                               \
class ALIAS_NAME {                                                              \
public:                                                                         \
    typedef T Type;                                                             \
    typedef cyphal_serializer<T> serializer_type;                               \
    typedef cyphal_deserializer<T> deserializer_type;                           \
    static constexpr serializer_type serializer = T##_serialize_;               \
    static constexpr deserializer_type deserializer = T##_deserialize_;         \
    static constexpr size_t extent = T##_EXTENT_BYTES_;                         \
    static constexpr size_t buffer_size = T##_SERIALIZATION_BUFFER_SIZE_BYTES_; \
};

class CyphalInterface {
private:
    const CanardNodeID node_id;
    std::unique_ptr<AbstractCANProvider> provider;
    UtilityConfig& utilities;
public:
    CyphalInterface(CanardNodeID node_id, UtilityConfig& config, AbstractCANProvider* provider) :
		node_id(node_id), utilities(config), provider(provider) {};
    template <typename Provider, class Allocator, class... Args> static CyphalInterface* create_bss(
        std::byte* buffer,
        CanardNodeID node_id,
        typename Provider::Handler handler,
        size_t queue_len,
        Args&&... args,
        UtilityConfig& config
    ) {
        std::byte** inout_buffer = &buffer;
        AbstractCANProvider* provider  = Provider::template create_bss<Allocator>(inout_buffer, handler, node_id, queue_len, args..., config);
    
        std::byte* interface_ptr = *inout_buffer;
        auto interface = new (interface_ptr) CyphalInterface(node_id, config, provider);

        return interface;
    }
    template <typename Provider, class Allocator, class... Args> static std::shared_ptr<CyphalInterface> create_heap(
		CanardNodeID node_id,
		typename Provider::Handler handler,
		size_t queue_len,
		Args&&... args,
		UtilityConfig& config
	) {
		AbstractCANProvider* provider  = Provider::template create_heap<Allocator>(handler, node_id, queue_len, args..., config);

		return std::make_shared<CyphalInterface>(node_id, config, provider);
	}

    bool is_up() { return bool(provider); }
    size_t queue_size() { return provider->queue.size; }
    bool has_unsent_frames() {
        if (!provider)
            return false;
        return canardTxPeek(&provider->queue) != NULL;
    }
    void process_tx_once() {  // needed for finalization of the whole program
        if (!provider)
            return;
        provider->process_canard_tx();
    }

    void loop();
    void push(
        CanardMicrosecond tx_deadline_usec,
        const CanardTransferMetadata* metadata,
        size_t payload_size,
        const void* payload
    ) const;
    void subscribe(
        CanardPortID port_id,
        size_t extent,
        CanardTransferKind kind,
        CanardRxSubscription* subscription
    ) const;

    // TEMPLATES
    template <typename TypeAlias>
    inline void send(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        CanardPriority priority,
        CanardTransferKind transfer_kind,
        CanardNodeID to_node_id,
        uint64_t timeout_delta
    ) const;
    template <typename TypeAlias>
    inline void send_msg(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        uint64_t timeout_delta = DEFAULT_TIMEOUT_MICROS,
        CanardPriority priority = CanardPriorityNominal
    ) const;
    template <typename TypeAlias>
    inline void send_response(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardRxTransfer* transfer,
        CanardPortID port,
        uint64_t timeout_delta = DEFAULT_TIMEOUT_MICROS,
        CanardPriority priority = CanardPriorityNominal
    ) const;
    template <typename TypeAlias>
    inline void send_request(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        CanardNodeID to_node_id,
        uint64_t timeout_delta = DEFAULT_TIMEOUT_MICROS,
        CanardPriority priority = CanardPriorityNominal
    ) const;
    template <typename TypeAlias>
    inline void deserialize_transfer (
        typename TypeAlias::Type* obj,
        CanardRxTransfer* transfer
    ) const;
};

template <typename TypeAlias>
inline void CyphalInterface::send(
    typename TypeAlias::Type* obj,
    uint8_t buffer[],
    CanardPortID port,
    CanardTransferID *transfer_id,
    CanardPriority priority,
    CanardTransferKind transfer_kind,
    CanardNodeID to_node_id,
    uint64_t timeout_delta
) const {
    size_t cyphal_buf_size = TypeAlias::buffer_size;
    if (TypeAlias::serializer(obj, buffer, &cyphal_buf_size) < 0) {
        utilities.error_handler();
    }
    const CanardTransferMetadata cyphal_transfer_metadata = {
        .priority = priority,
        .transfer_kind = transfer_kind,
        .port_id = port,
        .remote_node_id = to_node_id,
        .transfer_id = *transfer_id,
    };
    push(
        utilities.micros_64() + timeout_delta,
        &cyphal_transfer_metadata,
        cyphal_buf_size,
        buffer
    );
    (*transfer_id)++;
}

template <typename TypeAlias>
inline void CyphalInterface::send_msg(
    typename TypeAlias::Type *obj,
    uint8_t buffer[],
    CanardPortID port,
    CanardTransferID *transfer_id,
    uint64_t timeout_delta,
    CanardPriority priority
) const {
    send<TypeAlias>(
        obj,
        buffer,
        port,
        transfer_id,
        priority,
        CanardTransferKindMessage,
        CANARD_NODE_ID_UNSET,
        timeout_delta
    );
}

template <typename TypeAlias>
inline void CyphalInterface::send_response(
    typename TypeAlias::Type *obj,
    uint8_t buffer[],
    CanardRxTransfer *transfer,
    CanardPortID port,
    uint64_t timeout_delta,
    CanardPriority priority
) const {
    size_t cyphal_buf_size = TypeAlias::buffer_size;
    if (TypeAlias::serializer(obj, buffer, &cyphal_buf_size) < 0) {
        utilities.error_handler();
    }
    const CanardTransferMetadata cyphal_transfer_metadata = {
            .priority = priority,
            .transfer_kind = CanardTransferKindResponse,
            .port_id = port,
            .remote_node_id = transfer->metadata.remote_node_id,
            .transfer_id = transfer->metadata.transfer_id,
    };
    push(
        utilities.micros_64() + timeout_delta,
        &cyphal_transfer_metadata,
        cyphal_buf_size,
        buffer
    );
}

template <typename TypeAlias>
inline void CyphalInterface::send_request(
    typename TypeAlias::Type* obj,
    uint8_t buffer[],
    CanardPortID port,
    CanardTransferID* transfer_id,
    CanardNodeID to_node_id,
    uint64_t timeout_delta,
    CanardPriority priority
) const {
    send<TypeAlias>(
        obj,
        buffer,
        port,
        transfer_id,
        priority,
        CanardTransferKindRequest,
        to_node_id,
        timeout_delta
    );
}

template <typename TypeAlias>
inline void CyphalInterface::deserialize_transfer(
    typename TypeAlias::Type *obj,
    CanardRxTransfer* transfer
) const {
    size_t inout_buf_size = TypeAlias::extent;
    if(TypeAlias::deserializer(obj, (uint8_t *) transfer->payload, &inout_buf_size) < 0 ) {
        utilities.error_handler();
    }
}

#include <memory>
#include "libcanard/canard.h"

typedef const std::shared_ptr<CyphalInterface> InterfacePtr;

template <typename T>
class AbstractSubscription : public IListener<CanardRxTransfer*> {
    typedef typename T::Type Type;
protected:
    CanardRxSubscription sub = {};
    InterfacePtr interface;

    void subscribe(CanardPortID port_id, CanardTransferKind kind) {
        sub.user_reference = reinterpret_cast<void*>(this);
        interface->subscribe(port_id, T::extent, kind, &sub);
    }

    virtual void handler(const Type&, CanardRxTransfer*) = 0;
public:
    AbstractSubscription(InterfacePtr interface, CanardPortID port_id)
        : AbstractSubscription(interface, port_id, CanardTransferKindMessage) {};
    AbstractSubscription(
        InterfacePtr interface,
        CanardPortID port_id,
        CanardTransferKind kind
    ): interface(interface) {
        subscribe(port_id, kind);
    };

    void accept(CanardRxTransfer* transfer) {
        Type object;
        interface->deserialize_transfer<T>(&object, transfer);
        handler(object, transfer);
    }
};
