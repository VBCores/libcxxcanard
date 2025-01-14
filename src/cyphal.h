
#undef Error_Handler
#undef Error_Handler()
#define STM32_G
#define HAL_FDCAN_MODULE_ENABLED

#include <functional>

#if defined(STM32G474xx) || defined(STM32_G)
#include "stm32g4xx_hal.h"
#include "stm32g4xx_hal_fdcan.h"
// TODO: rework this dependency
#if __has_include("voltbro/utils.h")
    #include "voltbro/utils.h"
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
    AbstractAllocator(size_t size, const UtilityConfig& utilities) : utilities(utilities){};

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

    [[nodiscard]] const O1HeapInstance* const get_heap() const { return o1heap; }
};


/**
 * Наивный менеджер памяти, просто обертка вокруг malloc и free.
 */
class SystemAllocator : public AbstractAllocator {
public:
    // TODO: do something with size value?
    explicit SystemAllocator(size_t size, const UtilityConfig& utilities)
        : AbstractAllocator(size, utilities){};
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
// 32 cycles ~~ 200 ns delay for 160Mhz core clock
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
#if (defined(STM32G474xx) || defined(STM32_G)) && defined(HAL_FDCAN_MODULE_ENABLED)


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
        Args&&... args,
        const UtilityConfig& utilities
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

HAL_StatusTypeDef apply_filter(G4CAN::Handler hfdcan, FDCAN_FilterTypeDef* hw_filter, const CanardFilter& filter);

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
        Args&&... args,
        const UtilityConfig& config
    ) {
        std::byte** inout_buffer = &buffer;
        AbstractCANProvider* provider = Provider::template create_bss<Allocator>(
            inout_buffer,
            handler,
            node_id,
            queue_len,
            std::forward<Args>(args)...,
            config
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

#include <memory>
#include "libcanard/canard.h"

using InterfacePtr = const std::shared_ptr<CyphalInterface>;

/**
 * TODO
*/
template <typename T>
class AbstractSubscription : public IListener<CanardRxTransfer*> {
    using Type = typename T::Type;

protected:
    const CanardTransferKind kind;
    CanardRxSubscription sub = {};
    InterfacePtr interface;

    void subscribe(CanardPortID port_id) {
        sub.user_reference = static_cast<void*>(this);
        interface->subscribe(port_id, T::extent, kind, &sub);
    }

    virtual void handler(const Type&, CanardRxTransfer*) = 0;

public:
    // NOLINTBEGIN(modernize-pass-by-value)
    AbstractSubscription(InterfacePtr& interface, CanardPortID port_id)
        : AbstractSubscription(interface, port_id, CanardTransferKindMessage){};
    AbstractSubscription(InterfacePtr& interface, CanardPortID port_id, CanardTransferKind kind)
        : kind(kind), interface(interface) {
        subscribe(port_id);
    };
    // NOLINTEND(modernize-pass-by-value)

    virtual CanardFilter make_filter(CanardNodeID node_id) {
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
        Type object;
        interface->deserialize_transfer<T>(&object, transfer);
        handler(object, transfer);
    }

    virtual ~AbstractSubscription() {};
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
            value.empty = (uavcan_primitive_Empty_1_0){};
        }

        register_access_response.value = value;
        AbstractSubscription<RegisterAccessRequest>::interface->send_response<RegisterAccessResponse>(
            &register_access_response, transfer
        );
    };
};
