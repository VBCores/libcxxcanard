Examples
========

Documentation examples
----------------------

The ``examples/`` directory inside ``libcxxcanard`` is part of the documentation
surface. It is not a workspace for building applications in-place.

``simple_echo.ino``
~~~~~~~~~~~~~~~~~~~

Small Arduino sketch that listens for ``Natural32`` on ``ECHO_RX_PORT_ID`` and
sends the same value back on ``ECHO_TX_PORT_ID``.

.. literalinclude:: ../examples/simple_echo.ino
   :language: cpp

``full_example.ino``
~~~~~~~~~~~~~~~~~~~~

Arduino sketch that demonstrates subscriptions, message publishing, service
responses, and registers.

.. literalinclude:: ../examples/full_example.ino
   :language: cpp

``cyphal_types.cmake``
~~~~~~~~~~~~~~~~~~~~~~

Default CMake helper that can be copied into a project's type directory.

.. literalinclude:: ../examples/cyphal_types.cmake
   :language: cmake

HiL project
-----------

The repository-level ``examples/simple_cyphal_project`` project is used for
Linux/SocketCAN and hardware-in-the-loop checks. It builds multiple executable
targets from one CMake file:

* ``simple_cyphal_app``: original Natural32 read/write smoke test.
* ``simple_echo_hil``: checks ``examples/simple_echo.ino``.
* ``full_example_hil``: checks telemetry, echo message, echo service, and
  register access against ``examples/full_example.ino``.

