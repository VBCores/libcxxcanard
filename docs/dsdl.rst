DSDL And CMake
==============

Generated files
---------------

For each DSDL type, the build generates two kinds of headers:

* Nunavut C headers, for example
  ``uavcan/primitive/scalar/Natural32_1_0.h``.
* C++ traits sidecars, for example
  ``uavcan/primitive/scalar/Natural32_1_0.hpp``.

Always include the ``.hpp`` file from C++ code:

.. code-block:: cpp

   #include <uavcan/primitive/scalar/Natural32_1_0.hpp>

   using Natural32 = uavcan_primitive_scalar_Natural32_1_0;

The sidecar includes the matching C header and specializes
``CyphalTypeTraits<T>``. ``CyphalInterface`` uses this traits specialization to
serialize and deserialize raw Nunavut C structs.

CMake helper
------------

The default helper is ``cyphal_add_dsdl_types()`` from
``libcxxcanard/examples/cyphal_types.cmake``. Copy it into your type directory
and include it from your project:

.. code-block:: cmake

   add_subdirectory(libcxxcanard)

   target_link_libraries(my_app PRIVATE libcxxcanard Threads::Threads)
   target_include_directories(my_app PRIVATE
       ${CMAKE_CURRENT_SOURCE_DIR}
       ${CMAKE_CURRENT_SOURCE_DIR}/libcxxcanard
       ${CMAKE_CURRENT_SOURCE_DIR}/libcxxcanard/libs
   )

   include(${CMAKE_CURRENT_SOURCE_DIR}/cyphal_types/cyphal_types.cmake)
   cyphal_add_dsdl_types(my_app
       TYPE_REPOS
           ${CMAKE_CURRENT_SOURCE_DIR}/cyphal_types/public_regulated_data_types
           ${CMAKE_CURRENT_SOURCE_DIR}/cyphal_types/my_vendor_types
   )

``cyphal_add_dsdl_types()``:

* Finds root namespaces inside the provided type repositories.
* Generates C headers and C++ traits into the build directory.
* Adds generated include directories to the target.
* Adds the same generated include directories to ``libcxxcanard`` when that
  target exists.
* Adds build dependencies so code generation runs before compilation.

Templates
---------

The C++ traits templates live in ``libcxxcanard/nunavut_templates``. They are
not copied into the type repository. The helper discovers them from the
``libcxxcanard`` CMake target property ``CYPHAL_TRAITS_TEMPLATES_DIR``.

If a non-standard project cannot call ``add_subdirectory(libcxxcanard)`` before
``cyphal_add_dsdl_types()``, set ``LIBCXXCANARD_CXX_TRAITS_TEMPLATES_DIR``
explicitly to the ``cxxcanard_traits`` template directory.

