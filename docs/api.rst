API Reference
=============

Core
----

.. doxygenclass:: CyphalInterface
   :members:

.. doxygenstruct:: UtilityConfig
   :members:

Types
-----

.. doxygenstruct:: CyphalTypeTraits
   :members:

Subscriptions
-------------

.. doxygenclass:: AbstractSubscription
   :members:

Providers
---------

.. doxygenclass:: AbstractCANProvider
   :members:

.. doxygenclass:: LinuxCAN
   :members:

``G4CAN`` is the STM32 FDCAN provider. It is compiled only when STM32 HAL FDCAN
macros are available, so it may not appear in generic Doxygen XML builds.

Allocators
----------

.. doxygenclass:: AbstractAllocator
   :members:

.. doxygenclass:: SystemAllocator
   :members:

.. doxygenclass:: O1Allocator
   :members:

Embedded Helpers
----------------

.. doxygenclass:: EmbeddedCyphal
   :members:

``ArduinoCyphal`` is the Arduino-facing ``EmbeddedCyphal`` wrapper. It is
compiled only under ``ARDUINO`` builds and is documented in the Arduino guide.

Registers
---------

.. doxygenclass:: RegistersHandler
   :members:

.. doxygenclass:: RegistersProxy
   :members:
