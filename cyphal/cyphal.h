#pragma once

#include <memory>
#include <thread>
#include <unistd.h>
#include <atomic>

#include "cyphal/definitions.h"
#include "providers/provider.h"

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

#include "cyphal.tpp"
