Документация libcxxcanard
=========================

Если лень читать
----------------
**Рекомедуемая конфигурация**: `CyphalInterface::create_heap`, `O1Allocator`, `DEFAULT_CONFIG`, провайдер зависимо от платформы.

Главный класс
-------------

`CyphalInterface` - главный и единственный открытый для пользователя класс, не считая `AbstractSubscription`.

.. doxygenclass:: CyphalInterface
   :members:

Провайдеры (/providers)
-----------------------

Конструкторами провайдеров лучше не пользоваться напрямую, их вызывает фабричный метод в CyphalInterface.
То, какой конструктор вызовется, зависит от переданных аргументов.

.. doxygenclass:: AbstractCANProvider
   :members:

.. doxygenclass:: LinuxCAN
   :members:

.. doxygenclass:: G4CAN
   :members:

Аллокаторы (/allocators)
------------------------

Конструкторами аллокаторов лучше не пользоваться напрямую, их вызывает фабричный метод в CyphalInterface.
То, какой конструктор вызовется, зависит от переданных аргументов.


.. doxygenclass:: AbstractAllocator
   :members:

.. doxygenclass:: SystemAllocator
   :members:

.. doxygenclass:: O1Allocator
   :members:

Подписки (/subscriptions)
-------------------------

.. doxygenclass:: AbstractSubscription
   :members:

Утилиты
-------

.. doxygenstruct:: UtilityConfig
   :members:
