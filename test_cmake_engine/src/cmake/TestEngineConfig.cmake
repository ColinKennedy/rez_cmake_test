get_filename_component(CUSTOM_SCHEMAS_DIRECTORY "${CMAKE_CURRENT_LIST_FILE}" PATH)

if(NOT TARGET test_engine::test_engine)
    include("${CUSTOM_SCHEMAS_DIRECTORY}/TestEngineTargets.cmake")
endif()
