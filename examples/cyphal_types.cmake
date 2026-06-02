set(CYPHAL_TYPES_CMAKE_DIR "${CMAKE_CURRENT_LIST_DIR}")

function(cyphal_collect_root_namespaces OUT_VAR)
    set(ROOT_NAMESPACE_DIRS "")

    foreach(TYPE_REPO IN LISTS ARGN)
        if(NOT IS_DIRECTORY "${TYPE_REPO}")
            message(FATAL_ERROR "Cyphal type repository `${TYPE_REPO}` does not exist")
        endif()

        file(GLOB DIRECT_DSDL_FILES CONFIGURE_DEPENDS "${TYPE_REPO}/*.dsdl")
        if(DIRECT_DSDL_FILES)
            list(APPEND ROOT_NAMESPACE_DIRS "${TYPE_REPO}")
            continue()
        endif()

        file(GLOB CHILD_DIRS LIST_DIRECTORIES true "${TYPE_REPO}/*")
        foreach(CHILD_DIR IN LISTS CHILD_DIRS)
            if(NOT IS_DIRECTORY "${CHILD_DIR}")
                continue()
            endif()

            file(GLOB_RECURSE CHILD_DSDL_FILES CONFIGURE_DEPENDS "${CHILD_DIR}/*.dsdl")
            if(CHILD_DSDL_FILES)
                list(APPEND ROOT_NAMESPACE_DIRS "${CHILD_DIR}")
            endif()
        endforeach()
    endforeach()

    list(REMOVE_DUPLICATES ROOT_NAMESPACE_DIRS)
    set(${OUT_VAR} "${ROOT_NAMESPACE_DIRS}" PARENT_SCOPE)
endfunction()

function(cyphal_add_dsdl_types TARGET_NAME)
    set(ONE_VALUE_ARGS OUTPUT_DIR NUNAVUT_VERSION)
    set(MULTI_VALUE_ARGS TYPE_REPOS ROOT_NAMESPACES)
    cmake_parse_arguments(CYPHAL_TYPES "" "${ONE_VALUE_ARGS}" "${MULTI_VALUE_ARGS}" ${ARGN})

    if(NOT TARGET ${TARGET_NAME})
        message(FATAL_ERROR "Target `${TARGET_NAME}` does not exist")
    endif()

    if(NOT CYPHAL_TYPES_NUNAVUT_VERSION)
        set(CYPHAL_TYPES_NUNAVUT_VERSION "2.3.1")
    endif()

    if(NOT CYPHAL_TYPES_OUTPUT_DIR)
        set(CYPHAL_TYPES_OUTPUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/cyphal_types")
    endif()

    if(CYPHAL_TYPES_ROOT_NAMESPACES)
        set(CYPHAL_ROOT_NAMESPACE_DIRS "${CYPHAL_TYPES_ROOT_NAMESPACES}")
    else()
        if(NOT CYPHAL_TYPES_TYPE_REPOS)
            set(CYPHAL_TYPES_TYPE_REPOS "${CYPHAL_TYPES_CMAKE_DIR}")
        endif()
        cyphal_collect_root_namespaces(CYPHAL_ROOT_NAMESPACE_DIRS ${CYPHAL_TYPES_TYPE_REPOS})
    endif()

    if(NOT CYPHAL_ROOT_NAMESPACE_DIRS)
        message(FATAL_ERROR "No Cyphal DSDL namespaces found")
    endif()

    set(CYPHAL_GENERATED_C_DIR "${CYPHAL_TYPES_OUTPUT_DIR}/c")
    set(CYPHAL_GENERATED_TRAITS_DIR "${CYPHAL_TYPES_OUTPUT_DIR}/traits")
    set(CYPHAL_DSDL_CODEGEN_TARGET "${TARGET_NAME}_cyphal_dsdl_codegen")
    set(CYPHAL_DSDL_CODEGEN_STAMP "${CYPHAL_TYPES_OUTPUT_DIR}/.stamp")
    if(TARGET libcxxcanard)
        get_target_property(CYPHAL_TRAITS_TEMPLATES_DIR libcxxcanard CYPHAL_TRAITS_TEMPLATES_DIR)
    elseif(DEFINED LIBCXXCANARD_CXX_TRAITS_TEMPLATES_DIR)
        set(CYPHAL_TRAITS_TEMPLATES_DIR "${LIBCXXCANARD_CXX_TRAITS_TEMPLATES_DIR}")
    else()
        set(CYPHAL_TRAITS_TEMPLATES_DIR "${CYPHAL_TYPES_CMAKE_DIR}/templates/cxxcanard_traits")
    endif()
    if(NOT CYPHAL_TRAITS_TEMPLATES_DIR OR NOT IS_DIRECTORY "${CYPHAL_TRAITS_TEMPLATES_DIR}")
        message(FATAL_ERROR
            "libcxxcanard Nunavut C++ traits templates were not found. "
            "Call `add_subdirectory(libcxxcanard)` before `cyphal_add_dsdl_types(...)`, "
            "or set LIBCXXCANARD_CXX_TRAITS_TEMPLATES_DIR explicitly."
        )
    endif()

    set(CYPHAL_DSDL_FILES "")
    foreach(ROOT_NAMESPACE_DIR IN LISTS CYPHAL_ROOT_NAMESPACE_DIRS)
        file(GLOB_RECURSE ROOT_DSDL_FILES CONFIGURE_DEPENDS "${ROOT_NAMESPACE_DIR}/*.dsdl")
        list(APPEND CYPHAL_DSDL_FILES ${ROOT_DSDL_FILES})
    endforeach()
    file(GLOB CYPHAL_TRAITS_TEMPLATE_FILES CONFIGURE_DEPENDS "${CYPHAL_TRAITS_TEMPLATES_DIR}/*.j2")

    find_program(CYPHAL_NNVG_EXECUTABLE NAMES nnvg HINTS "$ENV{HOME}/.local/bin")
    find_program(CYPHAL_UV_EXECUTABLE NAMES uv HINTS "$ENV{HOME}/.local/bin")

    if(CYPHAL_NNVG_EXECUTABLE)
        set(CYPHAL_DSDL_GENERATOR_COMMAND ${CYPHAL_NNVG_EXECUTABLE})
    elseif(CYPHAL_UV_EXECUTABLE)
        set(CYPHAL_DSDL_GENERATOR_COMMAND
            ${CYPHAL_UV_EXECUTABLE}
            run
            --with
            nunavut==${CYPHAL_TYPES_NUNAVUT_VERSION}
            python
            -m
            nunavut
        )
    else()
        message(FATAL_ERROR "Cyphal DSDL generator was not found. Install `nnvg` or `uv`.")
    endif()

    set(CYPHAL_DSDL_LOOKUP_ARGS "")
    foreach(ROOT_NAMESPACE_DIR IN LISTS CYPHAL_ROOT_NAMESPACE_DIRS)
        list(APPEND CYPHAL_DSDL_LOOKUP_ARGS --lookup-dir "${ROOT_NAMESPACE_DIR}")
    endforeach()

    set(CYPHAL_DSDL_GENERATION_COMMANDS "")
    foreach(ROOT_NAMESPACE_DIR IN LISTS CYPHAL_ROOT_NAMESPACE_DIRS)
        list(APPEND CYPHAL_DSDL_GENERATION_COMMANDS
            COMMAND
                ${CYPHAL_DSDL_GENERATOR_COMMAND}
                --target-language c
                --language-standard c11
                --outdir "${CYPHAL_GENERATED_C_DIR}"
                ${CYPHAL_DSDL_LOOKUP_ARGS}
                "${ROOT_NAMESPACE_DIR}"
            COMMAND
                ${CYPHAL_DSDL_GENERATOR_COMMAND}
                --target-language c
                --language-standard c11
                --templates "${CYPHAL_TRAITS_TEMPLATES_DIR}"
                --output-extension hpp
                --generate-support never
                --outdir "${CYPHAL_GENERATED_TRAITS_DIR}"
                ${CYPHAL_DSDL_LOOKUP_ARGS}
                "${ROOT_NAMESPACE_DIR}"
        )
    endforeach()

    add_custom_command(
        OUTPUT "${CYPHAL_DSDL_CODEGEN_STAMP}"
        COMMAND ${CMAKE_COMMAND} -E make_directory "${CYPHAL_GENERATED_C_DIR}"
        COMMAND ${CMAKE_COMMAND} -E make_directory "${CYPHAL_GENERATED_TRAITS_DIR}"
        ${CYPHAL_DSDL_GENERATION_COMMANDS}
        COMMAND ${CMAKE_COMMAND} -E touch "${CYPHAL_DSDL_CODEGEN_STAMP}"
        DEPENDS ${CYPHAL_DSDL_FILES} ${CYPHAL_TRAITS_TEMPLATE_FILES}
        VERBATIM
    )

    add_custom_target(${CYPHAL_DSDL_CODEGEN_TARGET} DEPENDS "${CYPHAL_DSDL_CODEGEN_STAMP}")

    set(CYPHAL_DSDL_CONSUMER_TARGETS "${TARGET_NAME}")
    if(TARGET libcxxcanard AND NOT TARGET_NAME STREQUAL "libcxxcanard")
        list(APPEND CYPHAL_DSDL_CONSUMER_TARGETS libcxxcanard)
    endif()

    foreach(CONSUMER_TARGET IN LISTS CYPHAL_DSDL_CONSUMER_TARGETS)
        add_dependencies(${CONSUMER_TARGET} ${CYPHAL_DSDL_CODEGEN_TARGET})
        target_include_directories(${CONSUMER_TARGET} BEFORE PRIVATE
            "${CYPHAL_GENERATED_TRAITS_DIR}"
            "${CYPHAL_GENERATED_C_DIR}"
        )
    endforeach()
endfunction()

if(DEFINED CYPHAL_TYPES_TARGET)
    cyphal_add_dsdl_types(${CYPHAL_TYPES_TARGET} TYPE_REPOS "${CYPHAL_TYPES_CMAKE_DIR}")
endif()
