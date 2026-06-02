Linux And SocketCAN
===================

Provider
--------

Linux projects use ``LinuxCAN``. The handler argument is the SocketCAN interface
name, for example ``can0`` or ``vcan1.3``.

.. code-block:: cpp

   UtilityConfig utilities(
       _micros_64,
       []() {
           std::cerr << "Cyphal error" << std::endl;
           std::exit(1);
       }
   );

   auto interface = CyphalInterface::create_heap<LinuxCAN, SystemAllocator>(
       42,
       "vcan1.3",
       64,
       utilities
   );

Manual loop
-----------

The simplest integration is a normal loop:

.. code-block:: cpp

   while (running) {
       interface->loop();
   }

This processes RX and TX in the current thread.

Threaded loop
-------------

For Linux only, ``CyphalInterface`` can run RX and TX processing in background
threads:

.. code-block:: cpp

   interface->start_threads();

After that, subscription handlers are called from the RX thread and queued
transfers are flushed from the TX thread. The interface destructor stops the
threads; call ``stop_all_threads()`` explicitly when a deterministic shutdown
point is useful.

Ping-pong example
-----------------

This example sends the first ``Natural32`` ping, then sends the next ping from
the response handler:

.. code-block:: cpp

   #include <cstdlib>
   #include <iostream>
   #include <memory>

   #include <cyphal/allocators/sys/sys_allocator.h>
   #include <cyphal/cyphal.h>
   #include <cyphal/providers/LinuxCAN.h>
   #include <cyphal/subscriptions/subscription.h>

   #include <uavcan/primitive/scalar/Natural32_1_0.hpp>

   using Natural32 = uavcan_primitive_scalar_Natural32_1_0;

   constexpr CanardPortID PING_PORT_ID = 5000;
   constexpr CanardPortID PONG_PORT_ID = 5001;

   class Natural32PingPong : public AbstractSubscription<Natural32> {
   public:
       Natural32PingPong(InterfacePtr& interface)
           : AbstractSubscription<Natural32>(interface, PONG_PORT_ID),
             interface(interface) {}

   private:
       InterfacePtr interface;
       CanardTransferID transfer_id = 0;

       void handler(const Natural32& msg, CanardRxTransfer*) override {
           std::cout << "pong=" << msg.value << std::endl;

           Natural32 ping{};
           ping.value = msg.value + 1;
           interface->send_msg(&ping, PING_PORT_ID, &transfer_id);
       }
   };

   int main() {
       UtilityConfig utilities(
           _micros_64,
           []() {
               std::cerr << "Cyphal error" << std::endl;
               std::exit(1);
           }
       );

       auto interface = CyphalInterface::create_heap<LinuxCAN, SystemAllocator>(
           42,
           "vcan1.3",
           64,
           utilities
       );
       InterfacePtr interface_ref = interface;

       Natural32PingPong ping_pong(interface_ref);

       CanardTransferID transfer_id = 0;
       Natural32 first_ping{};
       first_ping.value = 1;
       interface->send_msg(&first_ping, PING_PORT_ID, &transfer_id);

       interface->start_threads();
   }

