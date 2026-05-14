
#undef Error_Handler
#undef Error_Handler()
                
#ifdef ARDUINO
extern "C" {
void __attribute__((weak, noreturn)) exit(int _) {
    while(true){};
}
}
#endif
#define STM32G4
#define HAL_FDCAN_MODULE_ENABLED

#include <functional>

#if defined(STM32G4)
#include "stm32g4xx_hal.h"
#include "stm32g4xx_hal_fdcan.h"
#elif defined(STM32G0)
#include "stm32g0xx.h"
#include "stm32g0xx_hal.h"
#include "stm32g0xx_hal_fdcan.h"
#endif
#if defined(STM32G4) || defined(STM32G0)
// TODO: rework this dependency
#if __has_include("voltbro/utils.hpp")
    #include "voltbro/utils.hpp"
#else
    #define CRITICAL_SECTION(code) code
#endif
#else
#define CRITICAL_SECTION(code) code
#include <unistd.h>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <utility>
#endif

// timestamp conversion macros
#define SEC_TO_US(sec) ((sec) * 1000000)
#define NS_TO_US(ns) ((ns) / 1000)

#ifdef __linux__
uint64_t _micros_64();
#endif

// NOLINTBEGIN(cppcoreguidelines-avoid-const-or-ref-data-members)
/**
 * Коллекция разных функций, требуемых для работы cyphal: микросекунды и обработчик ошибок.
 * Не очень типично для linux, но привычно на stm32 - поэтому используется везде ради кроссплатформенности.
*/
struct UtilityConfig {
    using micros_64_type = std::function<uint64_t()>;
    using error_handler_type = std::function<void()>;

    const micros_64_type micros_64;
    const error_handler_type error_handler;

    /**
     * @param micros Функция (функтор), возвращающая `uint64_t` микросекунды
     * @param handler Функция - "*что делать при ошибке*". На stm32 обычно просто `Error_Handler`, на linux - что угодно, можно просто `exit()`.
    */
    explicit UtilityConfig(micros_64_type&& micros, error_handler_type&& handler) noexcept
        : micros_64(std::forward<micros_64_type>(micros)),
          error_handler(std::forward<error_handler_type>(handler)){};
};
// NOLINTEND(cppcoreguidelines-avoid-const-or-ref-data-members)

#ifdef __linux__
extern const UtilityConfig DEFAULT_CONFIG;
#endif

template <typename T>
class IListener {
public:
    virtual void accept(T) = 0;
    virtual ~IListener() = default;
};

#include <tuple>
#include <type_traits>

#include "libcanard/canard.h"

/**
 * Абстрактный менеджер памяти. Сам по себе ничего не делает, вместо него надо передавать экземпляр
 * наследника - `o1` или `sys`.
 */
class AbstractAllocator {
protected:
    const UtilityConfig& utilities;

public:
    AbstractAllocator(const UtilityConfig& utilities) : utilities(utilities){};

    AbstractAllocator(const AbstractAllocator&) = delete;
    AbstractAllocator& operator=(const AbstractAllocator&) = delete;
    AbstractAllocator(AbstractAllocator&&) = delete;
    AbstractAllocator& operator=(AbstractAllocator&&) = delete;

    virtual void* allocate(CanardInstance* ins, size_t amount) = 0;
    virtual void free(CanardInstance* ins, void* pointer) = 0;
    virtual ~AbstractAllocator() = default;
};

#include "o1heap/o1heap.h"


/**
 * Обертка вокруг O1Heap. Рекомендуемый аллокатор для cyphal. Можем аллоцировать память для себя сам при создании,
 * может принять указатель на заранее выделенный участок.
 */
class O1Allocator : public AbstractAllocator {
private:
    O1HeapInstance* o1heap = nullptr;
    void* memory_arena;
    void align_self(size_t size);
    bool is_self_allocated = false;

public:
    /**
     * Создать на основе заранее выделенной памяти.
     *
     * @param size Размер буффера
     * @param memory Указатель на выделенный сегмент
     */
    O1Allocator(size_t size, void* memory, const UtilityConfig& utilities);
    /**
     * Создать аллокатор, который выдеит себя память сам.
     *
     * @param size Размер буффера
     */
    explicit O1Allocator(size_t size, const UtilityConfig& utilities);
    ~O1Allocator() override;

    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;

    [[nodiscard]] const O1HeapInstance* get_heap() const { return o1heap; }
};


/**
 * Наивный менеджер памяти, просто обертка вокруг malloc и free.
 */
class SystemAllocator : public AbstractAllocator {
public:

    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunused-parameter"
    // NOTE: <size> parameter required by the interface, but not used in this implementation
    // TODO: do something with size value?
    explicit SystemAllocator(size_t size, const UtilityConfig& utilities)
        : AbstractAllocator(utilities){};
    #pragma GCC diagnostic pop
    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;
};

#include <array>
#include <cstdint>


extern const std::array<uint32_t, 65> CanardFDCANLengthToDLC;
extern size_t fdcan_dlc_to_len(uint32_t);

#include <functional>
#include <memory>
#ifdef __linux__
#include <iostream>
#endif

#include "libcanard/canard.h"

extern std::unique_ptr<AbstractAllocator> _alloc_ptr;

inline void* alloc_f(CanardInstance* ins, size_t amount) {
    if (!_alloc_ptr) {
#ifdef __linux__
        std::cerr << "Tried to allocate canard memory before creating provider&allocator!"
                  << std::endl;
#endif
        exit(1);
    }
    return _alloc_ptr->allocate(ins, amount);
}
inline void free_f(CanardInstance* ins, void* pointer) {
    if (!_alloc_ptr) {
#ifdef __linux__
        std::cerr << "Tried to free (?) canard memory before creating provider&allocator!"
                  << std::endl;
#endif
        exit(1);
    }
    return _alloc_ptr->free(ins, pointer);
}

// 1 for tx, 1 for rx, 0.5 for misc (subs, multipart msgs, etc.)
constexpr float QUEUE_SIZE_MULT = 2.5F;
constexpr size_t DEFAULT_QUEUE_SIZE = 200;

/**
 * Абстрактная обертка вокруг основного функционала CAN.
 */
class AbstractCANProvider {
    friend class CyphalInterface;

protected:
    const size_t CANARD_MTU;
    const size_t WIRE_MTU;
    CanardTxQueue queue;
    CanardInstance canard;
    const UtilityConfig& utilities;

    AbstractCANProvider(size_t canard_mtu, size_t wire_mtu, const UtilityConfig& utilities)
        : AbstractCANProvider(canard_mtu, wire_mtu, DEFAULT_QUEUE_SIZE, utilities){};
    AbstractCANProvider(
        size_t canard_mtu,
        size_t wire_mtu,
        size_t queue_len,
        const UtilityConfig& utilities
    )
        : CANARD_MTU(canard_mtu),
          WIRE_MTU(wire_mtu),
          queue(canardTxInit(queue_len, CANARD_MTU)),
          utilities(utilities){};

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

    virtual void lock_canard() {};
    virtual void unlock_canard() {};
public:
    using Handler = void;

    AbstractCANProvider() = delete;
    AbstractCANProvider(const AbstractCANProvider&) = delete;
    AbstractCANProvider& operator=(const AbstractCANProvider&) = delete;
    AbstractCANProvider(AbstractCANProvider&&) = delete;
    AbstractCANProvider& operator=(AbstractCANProvider&&) = delete;

    virtual uint32_t len_to_dlc(size_t len) = 0;
    virtual size_t dlc_to_len(uint32_t dlc) = 0;
    virtual void can_loop(bool no_tx=false) = 0;
    virtual bool read_frame(CanardFrame*, void* data) = 0;
    virtual int write_frame(const CanardTxQueueItem* ti) = 0;
    void process_canard_rx(CanardFrame*);
    void process_canard_tx();
    void clear_queue();

    virtual ~AbstractCANProvider();
};

// Time to transmit one frame + delay for 25ns bit time ~ (25*29 (ext id) + 25*64 (body)) * 1.5
constexpr int ONE_FULL_FRAME_T = 2620;
// Cycles = ONE_FULL_FRAME_T / 200 * 32
constexpr int ONE_FULL_FRAME_CYCLES = 420;
// 32 cycles ~~ 200 ns delay for 160MHz core clock
constexpr int CYCLES_200NS_DELAY_DEFAULT = 32;

__attribute__((optimize("O1"))) static inline void delay_cycles(
    uint16_t cycles = CYCLES_200NS_DELAY_DEFAULT
) {
    /* Reference:
     https://developer.arm.com/documentation/ddi0439/b/Programmers-Model/Instruction-set-summary/Cortex-M4-instructions?lang=en
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
       bxeq    lr                 // 1 такт ("Conditional branch completes in a single cycle if the
     branch is not taken.")
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
    constexpr uint8_t SETUP_CYCLES = 8;
    constexpr uint8_t LOOP_CYCLES = 5;

    uint8_t real_cycles = (cycles - SETUP_CYCLES) / LOOP_CYCLES;
    while (real_cycles--) {
        // NOLINTBEGIN(hicpp-no-assembler)
        __asm__("nop");
        // NOLINTEND(hicpp-no-assembler)
    }
}
#if (defined(STM32G) || defined(STM32G4) || defined(STM32G0)) && defined(HAL_FDCAN_MODULE_ENABLED)


#include <utility>

/**
 * Реализация для stm32g4, работает на основне SocketCAN.
 * Аргументы для конструкторов смотри в `CyphalInterface::create_bss / CyphalInterface::create_heap` (фабричные методы).
*/
class G4CAN : public AbstractCANProvider {
public:
    using Handler = FDCAN_HandleTypeDef*;

private:
    FDCAN_HandleTypeDef* handler;
    G4CAN(Handler handler, size_t queue_len, const UtilityConfig& utilities)
        : AbstractCANProvider(CANARD_MTU_CAN_FD, 72, queue_len, utilities), handler(handler){};

public:
    template <class T, typename... Args>
    static G4CAN* create_bss(
        std::byte** inout_buffer,
        Handler handler,
        CanardNodeID node_id,
        size_t queue_len,
        const UtilityConfig& utilities,
        Args&&... args
    ) {
        std::byte* allocator_loc = *inout_buffer;
        // NOLINTBEGIN(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic,bugprone-narrowing-conversions,cppcoreguidelines-narrowing-conversions)
        auto allocator_ptr = new (allocator_loc) T(
            static_cast<size_t>(queue_len * sizeof(CanardTxQueueItem) * QUEUE_SIZE_MULT),
            std::forward<Args>(args)...,
            utilities
        );

        std::byte* provider_loc = allocator_loc + sizeof(T);
        auto ptr = new (provider_loc) G4CAN(handler, queue_len, utilities);
        // NOLINTEND(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic,bugprone-narrowing-conversions,cppcoreguidelines-narrowing-conversions)

        ptr->setup<T>(allocator_ptr, node_id);

        *inout_buffer = provider_loc + sizeof(G4CAN);
        return ptr;
    }

    template <class T, typename... Args>
    static G4CAN* create_heap(
        Handler handler,
        CanardNodeID node_id,
        size_t queue_len,
        Args&&... args,
        const UtilityConfig& utilities
    ) {
        // NOLINTBEGIN(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic,bugprone-narrowing-conversions,cppcoreguidelines-narrowing-conversions)
        auto allocator_ptr = new T(
            static_cast<size_t>(queue_len * sizeof(CanardTxQueueItem) * QUEUE_SIZE_MULT),
            args...,
            utilities
        );
        auto ptr = new G4CAN(handler, queue_len, utilities);
        // NOLINTEND(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic,bugprone-narrowing-conversions,cppcoreguidelines-narrowing-conversions)
        ptr->setup<T>(allocator_ptr, node_id);

        return ptr;
    }

    uint32_t len_to_dlc(size_t len) override;
    size_t dlc_to_len(uint32_t dlc) override;
    void can_loop(bool no_tx=false) override;
    bool read_frame(CanardFrame* frame, void* data) override;
    int write_frame(const CanardTxQueueItem* ti) override;
};

HAL_StatusTypeDef apply_filter(uint32_t filter_index, G4CAN::Handler hfdcan, const CanardFilter& filter);

#endif

#include <memory>
#include <thread>
#include <unistd.h>
#include <atomic>


constexpr uint64_t DEFAULT_TIMEOUT_MICROS = 1000000;  // 1 sec

template <typename ObjType>
using cyphal_serializer = int8_t (*)(const ObjType* const, uint8_t* const, size_t* const);
template <typename ObjType>
using cyphal_deserializer = int8_t (*)(ObjType* const, const uint8_t*, size_t* const);

// NOLINTBEGIN(cppcoreguidelines-macro-usage)

#define TYPE_ALIAS(ALIAS_NAME, T)                                                   \
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

// NOLINTEND(cppcoreguidelines-macro-usage)

/**
 * Основной класс со всей функциональностью. Это единственный класс непостредственно из этой библиотеки, экземплляр которого надо создать.
 */
class CyphalInterface {
private:
    const CanardNodeID node_id;
    const UtilityConfig& utilities;
    std::unique_ptr<AbstractCANProvider> provider;
#ifdef __linux__
    std::thread rx_thread;
    std::thread tx_thread;
    std::atomic<bool> threads_terminate_flag;
    std::atomic<bool> is_rx_terminated;
    std::atomic<bool> is_tx_terminated;
#endif

public:
    /**
     * Конструктор, позволяющий самому инициализировать AbstractCANProvider.
     * Не рекомендуется к использованию, **всегда** предпочитайте `create_bss` / `create_heap`.
    */
    CyphalInterface(
        CanardNodeID node_id,
        const UtilityConfig& config,
        AbstractCANProvider* provider
    )
        : node_id(node_id), utilities(config), provider(provider){};
    ~CyphalInterface();

    /**
     * Инициализировать CyphalInterface в глобальной памяти (.bss), не использует кучу.
     *
     * @param buffer Буффер размера `sizeof(CyphalInterface) + sizeof(выбранный_провайдер) + sizeof(выбранный_аллокатор)`
     * @param node_id ID текущей ноды
     * @param handler Низкоуровневый интерфейс CAN. Для linux просто строка "can0"/"can1". Для stm32 - обычно `&hfdcan1`.
     * @param queue_len Размер очереди сообщений
     * @param args Variadic параметры, которые будут переданы в provider.
     * @param config Ссылка на UtilityConfig.
    */
    template <typename Provider, class Allocator, class... Args>
    static CyphalInterface* create_bss(
        std::byte* buffer,
        CanardNodeID node_id,
        typename Provider::Handler handler,
        size_t queue_len,
        const UtilityConfig& config,
        Args&&... args
    ) {
        std::byte** inout_buffer = &buffer;
        AbstractCANProvider* provider = Provider::template create_bss<Allocator>(
            inout_buffer,
            handler,
            node_id,
            queue_len,
            config,
            std::forward<Args>(args)...
        );

        std::byte* interface_ptr = *inout_buffer;
        // NOLINTBEGIN(cppcoreguidelines-owning-memory)
        auto interface = new (interface_ptr) CyphalInterface(node_id, config, provider);
        // NOLINTEND(cppcoreguidelines-owning-memory)

        return interface;
    }
    /**
     * Инициализировать CyphalInterface на куче. Гораздо удобнее чем .bss, выделяет память только на старте программы и столько же сколько и `create_bss`,
     * поэтому если можете пользоваться кучей - пользуйтесь этим методом.
     *
     * @param node_id ID текущей ноды
     * @param handler Низкоуровневый интерфейс CAN. Для linux просто строка "can0"/"can1". Для stm32 - обычно `&hfdcan1`.
     * @param queue_len Размер очереди сообщений
     * @param args Variadic параметры, которые будут переданы в provider.
     * @param config Ссылка на UtilityConfig.
    */
    template <typename Provider, class Allocator, class... Args>
    static std::shared_ptr<CyphalInterface> create_heap(
        CanardNodeID node_id,
        typename Provider::Handler handler,
        size_t queue_len,
        Args&&... args,
        const UtilityConfig& config
    ) {
        AbstractCANProvider* provider = Provider::template create_heap<Allocator>(
            handler,
            node_id,
            queue_len,
            std::forward<Args>(args)...,
            config
        );

        return std::make_shared<CyphalInterface>(node_id, config, provider);
    }

    const UtilityConfig& get_utilities() const {
        return utilities;
    }
    /**
     * Проверка, инициализирован ли интерфейс (должна быть всегда `true`, если вы использовали `create_...`).
    */
    bool is_up() { return bool(provider); }
    /**
    * Количество FDCAN-сообщений в очереди на отправку.
    */
    size_t queue_size() {
        provider->lock_canard();
        size_t answer = provider->queue.size;
        provider->unlock_canard();
        return answer;
    }
    /**
    * Очистить очередь на отправку
    */
    void clear_queue() {
        provider->clear_queue();
    }
    /**
    * Есть ли еще не отправленные фреймы?
    */
    bool has_unsent_frames() {
        if (!provider) {
            return false;
        }
        provider->lock_canard();
        bool answer = canardTxPeek(&provider->queue) != nullptr;
        provider->unlock_canard();
        return answer;
    }
    /**
    * Прокрутить логику обработки исходящих сообщений *один раз*.
    */
    void process_tx_once() {  // needed for finalization of the whole program
        if (!provider) {
            return;
        }
        provider->process_canard_tx();
    }

    /**
    * Обрабатывать входящие/исходящие сообщения. НЕ бесконечный цикл, характерное использование:
    * ```
    * while (...) {
    *   interface->loop();
    * }
    * ```
    */
    void loop();
#ifdef __linux__
    void start_threads(uint64_t tx_delay_micros = 50);
    void stop_all_threads();
#endif

    void push(
        CanardMicrosecond tx_deadline_usec,
        const CanardTransferMetadata* metadata,
        size_t payload_size,
        const void* payload
    ) const;
    void unsubscribe(CanardPortID port_id, CanardTransferKind kind);
    // TEMPLATES
    template <typename TypeAlias>
    void subscribe(
        CanardPortID port_id,
        CanardTransferKind kind,
        CanardRxSubscription* subscription
    );
    template <typename TypeAlias>
    inline void send(
        typename TypeAlias::Type* obj,
        CanardPortID port,
        CanardTransferID* transfer_id,
        CanardPriority priority,
        CanardTransferKind transfer_kind,
        CanardNodeID to_node_id,
        uint64_t timeout_delta
    ) const;

    /**
    * Поставить одно сообщение в очередь на отправку.
    *
    * @param obj Указатель на сообщение (cyphal-структура)
    * @param port PortID назначения
    * @param transfer_id TransferID - отдельные для каждого port и не забывайте инкрементировать!
    * @param timeout_delta Таймаут отправки в нс - по умочанию 1с
    * @param priority Приоритет сообщения
    */
    template <typename TypeAlias>
    inline void send_msg(
        typename TypeAlias::Type* obj,
        CanardPortID port,
        CanardTransferID* transfer_id,
        uint64_t timeout_delta = DEFAULT_TIMEOUT_MICROS,
        CanardPriority priority = CanardPriorityNominal
    ) const;
    /**
    * Отправить ответ на запрос.
    *
    * @param obj Указатель на сообщение (cyphal-структура)
    * @param transfer Структура CanardRxTransfer **полученная вместе с запросом**
    * @param timeout_delta Таймаут отправки в нс - по умочанию 1с
    */
    template <typename TypeAlias>
    inline void send_response(
        typename TypeAlias::Type* obj,
        CanardRxTransfer* transfer,
        uint64_t timeout_delta = DEFAULT_TIMEOUT_MICROS
    ) const;
    /**
    * Отправить запрос
    *
    * @param obj Указатель на сообщение (cyphal-структура)
    * @param port PortID назначения
    * @param transfer_id TransferID - отдельные для каждого port и не забывайте инкрементировать!
    * @param to_node_id NodeID узла назначения
    * @param timeout_delta Таймаут отправки в нс - по умочанию 1с
    * @param priority Приоритет сообщения
    */
    template <typename TypeAlias>
    inline void send_request(
        typename TypeAlias::Type* obj,
        CanardPortID port,
        CanardTransferID* transfer_id,
        CanardNodeID to_node_id,
        uint64_t timeout_delta = DEFAULT_TIMEOUT_MICROS,
        CanardPriority priority = CanardPriorityNominal
    ) const;
    template <typename TypeAlias>
    inline void deserialize_transfer(typename TypeAlias::Type* obj, CanardRxTransfer* transfer)
        const;
};

template <typename TypeAlias>
inline void CyphalInterface::send(
    typename TypeAlias::Type* obj,
    CanardPortID port,
    CanardTransferID *transfer_id,
    CanardPriority priority,
    CanardTransferKind transfer_kind,
    CanardNodeID to_node_id,
    uint64_t timeout_delta
) const {
    uint8_t buffer[TypeAlias::buffer_size];
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
    CanardPortID port,
    CanardTransferID *transfer_id,
    uint64_t timeout_delta,
    CanardPriority priority
) const {
    send<TypeAlias>(
        obj,
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
    CanardRxTransfer *transfer,
    uint64_t timeout_delta
) const {
    uint8_t buffer[TypeAlias::buffer_size];
    size_t cyphal_buf_size = TypeAlias::buffer_size;
    if (TypeAlias::serializer(obj, buffer, &cyphal_buf_size) < 0) {
        utilities.error_handler();
    }
    const CanardTransferMetadata cyphal_transfer_metadata = {
            .priority = transfer->metadata.priority,
            .transfer_kind = CanardTransferKindResponse,
            .port_id = transfer->metadata.port_id,
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
    CanardPortID port,
    CanardTransferID* transfer_id,
    CanardNodeID to_node_id,
    uint64_t timeout_delta,
    CanardPriority priority
) const {
    send<TypeAlias>(
        obj,
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

template <typename TypeAlias>
inline void CyphalInterface::subscribe(
    CanardPortID port_id,
    CanardTransferKind kind,
    CanardRxSubscription* subscription
) {
    if (canardRxSubscribe(
            (CanardInstance* const)&provider->canard,
            kind,
            port_id,
            TypeAlias::extent,
            CANARD_DEFAULT_TRANSFER_ID_TIMEOUT_USEC,
            subscription
        ) != 1) {
        utilities.error_handler();
    }
}

#include <memory>
#include <functional>

#include "libcanard/canard.h"

using InterfacePtr = const std::shared_ptr<CyphalInterface>;
using TransferListener = IListener<CanardRxTransfer*>;

class IHasFilter {
public:
    virtual CanardFilter make_filter(CanardNodeID node_id) = 0;
    virtual ~IHasFilter() = default;
};

/**
 * TODO docs
*/
template <typename T>
class AbstractSubscription : public TransferListener, public IHasFilter {
    using Type = typename T::Type;

protected:
    const CanardPortID port_id;
    const CanardTransferKind kind;
    InterfacePtr interface;
    CanardRxSubscription sub = {};

    virtual void handler(const Type&, CanardRxTransfer*) = 0;

public:
    // NOLINTBEGIN(modernize-pass-by-value)
    AbstractSubscription(InterfacePtr& interface, CanardPortID port_id)
        : AbstractSubscription(interface, port_id, CanardTransferKindMessage){};
    AbstractSubscription(InterfacePtr& interface, CanardPortID port_id, CanardTransferKind kind)
        : port_id(port_id), kind(kind), interface(interface) {
        sub.user_reference = static_cast<void*>(this);
        interface->subscribe<T>(port_id, kind, &sub);
    };
    // NOLINTEND(modernize-pass-by-value)

    CanardFilter make_filter(CanardNodeID node_id) override{
        CanardFilter out = {};

        switch (kind) {
            case CanardTransferKindMessage:
                out = canardMakeFilterForSubject(sub.port_id);
                break;
            case CanardTransferKindRequest:
            case CanardTransferKindResponse:
                out = canardMakeFilterForService(sub.port_id, node_id);
                break;
        }

        return out;
    }

    void accept(CanardRxTransfer* transfer) override {
        // NOTE: I would like to NOT initialize this object to save cpu cycles
        //       but whatever else I do triggers a compiler warning -Wmaybe-uninitialized.
        //       Its somehow related to flto step? Since it appears at linking step after flto logs,
        //       even with "GNU push ignore warning" pragmas. Weird stuff.
        Type object{};
        interface->deserialize_transfer<T>(&object, transfer);
        handler(object, transfer);
    }

    virtual ~AbstractSubscription() {
        interface->unsubscribe(port_id, kind);
    };
};

#include <string>
#include <utility>


#include <uavcan/node/GetInfo_1_0.h>

TYPE_ALIAS(NodeInfoRequest, uavcan_node_GetInfo_Request_1_0)
TYPE_ALIAS(NodeInfoResponse, uavcan_node_GetInfo_Response_1_0)

class NodeInfoReader : public AbstractSubscription<NodeInfoRequest> {
private:
    NodeInfoResponse::Type node_info;
public:
    NodeInfoReader(
        InterfacePtr interface,
        std::string&& name,
        uavcan_node_Version_1_0&& protocol_version,
        uavcan_node_Version_1_0&& hardware_version,
        uavcan_node_Version_1_0&& software_version,
        uint64_t software_vcs_revision_id
    );
    void handler(const NodeInfoRequest::Type&, CanardRxTransfer*) override;
};

#include <tuple>
#include <functional>
#include <utility>
#include <array>

#include "uavcan/_register/Name_1_0.h"

#include <uavcan/_register/Access_1_0.h>
#include <uavcan/_register/List_1_0.h>

TYPE_ALIAS(RegisterAccessRequest, uavcan_register_Access_Request_1_0)
TYPE_ALIAS(RegisterAccessResponse, uavcan_register_Access_Response_1_0)
TYPE_ALIAS(RegisterListRequest, uavcan_register_List_Request_1_0)
TYPE_ALIAS(RegisterListResponse, uavcan_register_List_Response_1_0)

using RegisterCallback = std::function<void(
    const uavcan_register_Value_1_0&,
    uavcan_register_Value_1_0&,
    RegisterAccessResponse::Type&
)>;
using RegisterDefinition = std::pair<std::string, RegisterCallback>;

template<size_t N>
class RegistersHandler:
        public AbstractSubscription<RegisterListRequest>,
        public AbstractSubscription<RegisterAccessRequest> {
private:
    std::array<RegisterDefinition, N> registers;
public:
    RegistersHandler(std::array<RegisterDefinition, N>&& registers_list, InterfacePtr interface):
        AbstractSubscription<RegisterListRequest>(
            interface,
            uavcan_register_List_1_0_FIXED_PORT_ID_,
            CanardTransferKindRequest
        ),
        AbstractSubscription<RegisterAccessRequest>(
            interface,
            uavcan_register_Access_1_0_FIXED_PORT_ID_,
            CanardTransferKindRequest
        ),
        registers(std::move(registers_list))
    {}

    virtual CanardFilter make_filter(CanardNodeID node_id) override {
        CanardFilter access_filter = AbstractSubscription<RegisterAccessRequest>::make_filter(node_id);
        CanardFilter list_filter = AbstractSubscription<RegisterListRequest>::make_filter(node_id);
        return canardConsolidateFilters(&access_filter, &list_filter);
    }

    void handler(const RegisterListRequest::Type& register_list_request, CanardRxTransfer* transfer) override {
        RegisterListResponse::Type register_list_response = {};

        uavcan_register_Name_1_0 name = {};

        if (register_list_request.index < registers.size()) {
            auto register_name = std::get<std::string>(registers[register_list_request.index]);
            memcpy(name.name.elements, register_name.c_str(), register_name.size());
            name.name.count = register_name.size();
        }
        register_list_response.name = name;

        AbstractSubscription<RegisterListRequest>::interface->send_response<RegisterListResponse>(
            &register_list_response, transfer
        );
    };

    void handler(const RegisterAccessRequest::Type& register_access_request, CanardRxTransfer* transfer) override {
        RegisterAccessResponse::Type register_access_response = {};

        InterfacePtr interface = AbstractSubscription<RegisterAccessRequest>::interface;

        register_access_response.timestamp.microsecond = interface->get_utilities().micros_64();
        uavcan_register_Value_1_0 value = {};

        bool is_found = false;
        for (auto& register_def : registers) {
            auto& register_name = std::get<std::string>(register_def);
            if(memcmp(
                register_name.c_str(),
                register_access_request.name.name.elements,
                register_access_request.name.name.count
            ) != 0) {
                continue;
            }
            is_found = true;
            auto& register_handler = std::get<RegisterCallback>(register_def);
            register_handler(register_access_request.value, value, register_access_response);
            break;
        }
        if (!is_found) {
            value._tag_ = 0;
            value.empty = {};
        }

        register_access_response.value = value;
        AbstractSubscription<RegisterAccessRequest>::interface->send_response<RegisterAccessResponse>(
            &register_access_response, transfer
        );
    };
};


static constexpr uint8_t REGISTER_EMPTY_TAG = 0U;
static constexpr uint8_t REGISTER_BIT_TAG = 3U;
static constexpr uint8_t REGISTER_REAL32_TAG = 13U;
static constexpr uint8_t REGISTER_NATURAL32_TAG = 9U;

inline bool parse_register_bit(const uavcan_register_Value_1_0& value, bool& parsed) {
    if (value._tag_ != REGISTER_BIT_TAG || value.bit.value.count == 0) {
        return false;
    }
    parsed = value.bit.value.bitpacked[0] == 1;
    return true;
}

inline bool parse_register_real32(const uavcan_register_Value_1_0& value, float& parsed) {
    if (value._tag_ != REGISTER_REAL32_TAG || value.real32.value.count == 0) {
        return false;
    }
    parsed = value.real32.value.elements[0];
    return true;
}

inline void fill_register_bit(uavcan_register_Value_1_0& out, bool value) {
    out._tag_ = REGISTER_BIT_TAG;
    out.bit.value.bitpacked[0] = value;
    out.bit.value.count = 1;
}

inline void fill_register_real32(uavcan_register_Value_1_0& out, float value) {
    out._tag_ = REGISTER_REAL32_TAG;
    out.real32.value.elements[0] = value;
    out.real32.value.count = 1;
}

inline void fill_register_natural32(uavcan_register_Value_1_0& out, uint32_t value) {
    out._tag_ = REGISTER_NATURAL32_TAG;
    out.natural32.value.elements[0] = value;
    out.natural32.value.count = 1;
}

#include <optional>
#include <functional>
#include <tuple>
#include <map>


class RegistersProxy: public AbstractSubscription<RegisterAccessResponse> {
private:
    std::map<CanardTransferID, std::tuple<std::string, uint64_t>> transfer_map;
    const CanardNodeID target_node_id;
    CanardTransferID register_access_transfer_id = 0;

    template <typename T>
    void request_generic(const std::string& name, std::optional<T> value, void(*filler)(uavcan_register_Value_1_0&, T)) {
        RegisterAccessRequest::Type request {0};
        size_t name_size = std::min(name.size(), size_t{255});
        memcpy(request.name.name.elements, name.c_str(), name_size);
        request.name.name.count = name_size;
        if (value) {
            filler(request.value, *value);
        }
        else {
            request.value._tag_ = REGISTER_EMPTY_TAG;
        }

        clean_transfer_map();
        transfer_map[register_access_transfer_id] = std::make_tuple(
            name,
            interface->get_utilities().micros_64() + DEFAULT_TIMEOUT_MICROS
        );
        interface->send_request<RegisterAccessRequest>(
            &request,
            uavcan_register_Access_1_0_FIXED_PORT_ID_,
            &register_access_transfer_id,
            target_node_id
        );
    }

#if __cplusplus >= 202002L
    // C++20: std::erase_if available natively
    void clean_transfer_map() {
        std::erase_if(
            transfer_map,
            [this](const auto& item) {
                const auto& [key, val] = item;
                return interface->get_utilities().micros_64() > std::get<uint64_t>(val);
            }
        );
    }
#else
    // C++17 fallback: manual iterator-based erase
    void clean_transfer_map() {
        const uint64_t now = interface->get_utilities().micros_64();
        for (auto it = transfer_map.begin(); it != transfer_map.end(); /* no increment */) {
            if (now > std::get<uint64_t>(it->second)) {
                it = transfer_map.erase(it); // erase returns the next valid iterator
            } else {
                ++it;
            }
        }
    }
#endif

public:
    RegistersProxy(
        InterfacePtr interface,
        CanardNodeID target_node_id
    ) :
        AbstractSubscription<RegisterAccessResponse>(
            interface,
            uavcan_register_Access_1_0_FIXED_PORT_ID_,
            CanardTransferKindResponse
        ),
        target_node_id(target_node_id)
    {}

    size_t pending_requests() {
        return transfer_map.size();
    }

    void request_real32_value(const std::string& name, std::optional<float> value = std::nullopt) {
        request_generic<float>(name, value, &fill_register_real32);
    }

    void request_natural32_value(const std::string& name, std::optional<uint32_t> value = std::nullopt) {
        request_generic<uint32_t>(name, value, &fill_register_natural32);
    }

    void handler(const RegisterAccessResponse::Type& register_response, CanardRxTransfer* transfer) override {
        if (transfer->metadata.remote_node_id != target_node_id) {
            return;
        }
        CanardTransferID key = transfer->metadata.transfer_id;
        if (transfer_map.count(key) == 0) {
            return;
        }
        const std::string& reg_name = std::get<std::string>(transfer_map[key]);
        switch (register_response.value._tag_) {
            case REGISTER_REAL32_TAG:
                handle_float32(reg_name, register_response.value.real32.value.elements[0], transfer);
                break;
            case REGISTER_NATURAL32_TAG:
                handle_natural32(reg_name, register_response.value.natural32.value.elements[0], transfer);
                break;
            default:
                break;
        }
        transfer_map.erase(key);
    };

    virtual void handle_float32(const std::string& name, float value, CanardRxTransfer* transfer) = 0;
    virtual void handle_natural32(const std::string& name, uint32_t value, CanardRxTransfer* transfer) = 0;
};

#if defined(STM32G0)
#include "stm32g0xx_hal.h"
#elif defined(STM32G4)
#include "stm32g4xx_hal.h"
#endif
#if defined(HAL_FDCAN_MODULE_ENABLED)

#include <functional>


#include <uavcan/diagnostic/Record_1_1.h>
#include <uavcan/node/Heartbeat_1_0.h>
#include <uavcan/node/Health_1_0.h>
#include <uavcan/node/Mode_1_0.h>

TYPE_ALIAS(DiagnosticRecord, uavcan_diagnostic_Record_1_1)
TYPE_ALIAS(HBeat, uavcan_node_Heartbeat_1_0)

// NOTE: MUST be implemented by user
#ifndef ARDUINO
#define millis_t millis
#define micros_t micros
millis_t millis_32();
micros_t micros_64();
#else
#include <Arduino.h>
#include "utils.h"
#define millis_t uint32_t
#define micros_t uint64_t
#define millis_32 millis
#define micros_64 micros
#endif

template<size_t QUEUE_SIZE, millis_t DELAY_ON_ERROR, size_t REGISTERS_COUNT>
class EmbeddedCyphal {
protected:
    bool _is_cyphal_on = false;
    uint8_t _health_status = uavcan_node_Health_1_0_NOMINAL;
    uint8_t _mode = uavcan_node_Mode_1_0_INITIALIZATION;
    millis_t _delay_cyphal_until_millis = 0;

    FDCAN_HandleTypeDef* hfdcan;
    UtilityConfig utilities;
    std::shared_ptr<CyphalInterface> cyphal_interface;
    std::byte cyphal_bss_buffer[
        sizeof(CyphalInterface) + sizeof(G4CAN) + sizeof(O1Allocator)
    ] __attribute__((aligned(4)));
    // Must match the arena size requested by G4CAN::create_bss().
    static const size_t CYPHAL_BUFFER_SIZE = static_cast<size_t>(
        QUEUE_SIZE * sizeof(CanardTxQueueItem) * QUEUE_SIZE_MULT
    );
    static inline std::byte cyphal_queue_buffer[CYPHAL_BUFFER_SIZE] __attribute__((aligned(O1HEAP_ALIGNMENT)));

    NodeInfoReader node_info_reader;
    RegistersHandler<REGISTERS_COUNT> registers_handler;

    void heartbeat() {
        static CanardTransferID hbeat_transfer_id = 0;
        HBeat::Type heartbeat_msg = {
            .uptime = (uint32_t)std::floor(millis_32() / 1000.0f),
            .health = {_health_status},
            .mode = {_mode},
            .vendor_specific_status_code = static_cast<uint8_t>(cyphal_interface->queue_size())
        };

        if (_is_cyphal_on) {
            cyphal_interface->send_msg<HBeat>(
                &heartbeat_msg,
                uavcan_node_Heartbeat_1_0_FIXED_PORT_ID_,
                &hbeat_transfer_id,
                MICROS_S * 2
            );
        }
    }

    void cyphal_error_handler() {
        _is_cyphal_on = false;
        cyphal_interface->clear_queue();
        // delay for half a second
        _delay_cyphal_until_millis = millis_32() + DELAY_ON_ERROR;
    }

    void restart_cyphal() {
        cyphal_interface->clear_queue();

        static CanardTransferID record_transfer_id = 0;
        DiagnosticRecord::Type record;
        record.severity.value = uavcan_diagnostic_Severity_1_0_ERROR;
        sprintf(reinterpret_cast<char*>(record.text.elements), "cyphal_error_handler was called internally");
        record.text.count = strlen((char*)record.text.elements);

        cyphal_interface->send_msg<DiagnosticRecord>(
                &record,
                uavcan_diagnostic_Record_1_1_FIXED_PORT_ID_,
                &record_transfer_id
        );

        _delay_cyphal_until_millis = 0;
        _is_cyphal_on = true;
    }

    void start_cyphal() {
        HAL_IMPORTANT(HAL_FDCAN_ConfigTxDelayCompensation(
            hfdcan,
            hfdcan->Init.DataTimeSeg1 * hfdcan->Init.DataPrescaler,
            0
        ))
        HAL_IMPORTANT(HAL_FDCAN_EnableTxDelayCompensation(hfdcan))
        HAL_IMPORTANT(HAL_FDCAN_Start(hfdcan))

        _is_cyphal_on = true;
    }

    void finish_cyphal_setup() {
        setup_subscriptions();
        start_cyphal();
    }

public:
    explicit EmbeddedCyphal(
        FDCAN_HandleTypeDef* hfdcan,
        CanardNodeID node_id,
        std::string&& name,
        std::array<RegisterDefinition, REGISTERS_COUNT>&& registers_list
    ):
        EmbeddedCyphal(
            hfdcan,
            node_id,
            std::move(name),
            uavcan_node_Version_1_0{1, 0},
            uavcan_node_Version_1_0{1, 0},
            uavcan_node_Version_1_0{1, 0},
            0,
            std::move(registers_list)
        )
    {}

    explicit EmbeddedCyphal(
        FDCAN_HandleTypeDef* hfdcan,
        CanardNodeID node_id,
        std::string&& name,
        uavcan_node_Version_1_0&& protocol_version,
        uavcan_node_Version_1_0&& hardware_version,
        uavcan_node_Version_1_0&& software_version,
        uint64_t software_vcs_revision_id,
        std::array<RegisterDefinition, REGISTERS_COUNT>&& registers_list
    ):
        hfdcan(hfdcan),
        utilities(micros_64, std::bind(&EmbeddedCyphal::cyphal_error_handler, this)),
        cyphal_interface(CyphalInterface::create_bss<G4CAN, O1Allocator>(
            cyphal_bss_buffer,
            node_id,
            hfdcan,
            QUEUE_SIZE,
            utilities,
            cyphal_queue_buffer
        )),
        node_info_reader(
            cyphal_interface,
            std::forward<std::string>(name),
            std::forward<uavcan_node_Version_1_0>(protocol_version),
            std::forward<uavcan_node_Version_1_0>(hardware_version),
            std::forward<uavcan_node_Version_1_0>(software_version),
            std::forward<uint64_t>(software_vcs_revision_id)
        ),
        registers_handler(
            std::forward<std::array<RegisterDefinition, REGISTERS_COUNT>>(registers_list),
            cyphal_interface
        )
        {}

    void set_mode(uint8_t mode) {
        _mode = mode;
    }

    void set_status(uint8_t status) {
        _health_status = status;
    }

    __attribute__((hot, flatten)) void cyphal_loop() {
        if (_is_cyphal_on) {
            cyphal_interface->loop();
        }
        if (_is_cyphal_on) {
            millis_t current_t = millis_32();
            in_loop_reporting(current_t);

            static millis_t heartbeat_time = 0;
            EACH_N(current_t, heartbeat_time, 1000, {
                heartbeat();
            })
        }

        if (_delay_cyphal_until_millis != 0 &&
            _delay_cyphal_until_millis <= millis_32()) {
            restart_cyphal();
        }
    }

    virtual void setup_subscriptions() {
        HAL_FDCAN_ConfigGlobalFilter(
            hfdcan,
            FDCAN_REJECT,
            FDCAN_REJECT,
            FDCAN_REJECT_REMOTE,
            FDCAN_REJECT_REMOTE
        );
    }

    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunused-parameter"
    // NOTE: <current_t> parameter required by the interface, but not used in this implementation
    virtual void in_loop_reporting(millis_t current_t) {
    #pragma GCC diagnostic pop
    }

    void begin() {
        finish_cyphal_setup();
        set_mode(uavcan_node_Mode_1_0_OPERATIONAL);
    }
};


#ifdef ARDUINO
template<size_t REGISTERS_COUNT = 0>
class ArduinoCyphal : public EmbeddedCyphal<128, 500, REGISTERS_COUNT> {
private:
    using Base = EmbeddedCyphal<128, 500, REGISTERS_COUNT>;

public:
    explicit ArduinoCyphal(
        FDCAN_HandleTypeDef* hfdcan,
        CanardNodeID node_id,
        std::string name = "org.voltbro.arduino.node",
        std::array<RegisterDefinition, REGISTERS_COUNT> registers_list = {}
    ):
        Base(
            hfdcan,
            node_id,
            std::move(name),
            std::move(registers_list)
        )
    {}

    void setup_subscriptions() override {
        HAL_IMPORTANT(HAL_FDCAN_ConfigGlobalFilter(
            this->hfdcan,
            FDCAN_ACCEPT_IN_RX_FIFO0,
            FDCAN_ACCEPT_IN_RX_FIFO0,
            FDCAN_REJECT_REMOTE,
            FDCAN_REJECT_REMOTE
        ));
    }
};
#undef millis_t
#undef micros_t
#undef millis_32
#undef micros_64
#endif

#endif
