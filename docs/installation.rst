Installation
============

Repository layout
-----------------

``libcxxcanard`` is intended to be used as a source dependency. A typical CMake
project layout looks like this:

.. code-block:: text

   my_project/
       CMakeLists.txt
       main.cpp
       libcxxcanard/
       cyphal_types/
           public_regulated_data_types/
           my_vendor_types/
           cyphal_types.cmake

The ``cyphal_types.cmake`` helper can be copied from
``libcxxcanard/examples/cyphal_types.cmake``. It does not need local Nunavut
``.j2`` templates. The C++ traits templates are shipped with ``libcxxcanard``
under ``nunavut_templates/`` and are discovered after
``add_subdirectory(libcxxcanard)``.

Required tools
--------------

For Linux/CMake projects:

* CMake 3.15 or newer.
* A C++17 compiler.
* ``libcxxcanard/libs/libcanard`` and ``libcxxcanard/libs/o1heap`` from this
  repository.
* ``nnvg`` or ``uv``. If ``nnvg`` is not installed, the helper runs Nunavut via
  ``uv run --with nunavut==... python -m nunavut``.
* DSDL type repositories, at least OpenCyphal public regulated data types.

For STM32 Arduino projects:

* Arduino CLI or Arduino IDE.
* STM32duino board package.
* ``libcxxcanard`` installed into the Arduino libraries directory.
* A generated/packed ``src/`` directory. This repository keeps ``src/`` as the
  Arduino-facing library layout.

For documentation builds:

* Doxygen.
* Sphinx.
* ``breathe`` and ``sphinx_rtd_theme`` from ``docs/requirements.txt``.

