libcxxcanard
============

``libcxxcanard`` is a small C++17 wrapper around OpenCyphal
`libcanard <https://github.com/OpenCyphal/libcanard>`_ and ``o1heap``.
It keeps the transport model close to the C implementation, but gives
application code a compact typed interface for sending messages, handling
subscriptions, answering services, and exposing Cyphal registers.

The library is used in three main shapes:

* Linux and normal CMake projects through SocketCAN and generated DSDL headers.
* STM32 bare-metal projects through the G4 FDCAN provider.
* STM32 Arduino projects through the packed Arduino library in ``src/``.

Current type model
------------------

Application code uses raw Nunavut-generated C structs directly. For example,
``uavcan_primitive_scalar_Natural32_1_0`` is the message type. A generated C++
traits sidecar, such as ``uavcan/primitive/scalar/Natural32_1_0.hpp``, registers
the serializer, deserializer, extent, and serialization buffer size for
``CyphalInterface``.

There is no legacy wrapper alias layer. Include ``.hpp`` generated sidecars in
C++ and Arduino code.

Contents
--------

.. toctree::
   :maxdepth: 2

   installation
   dsdl
   linux
   arduino
   examples
   api

