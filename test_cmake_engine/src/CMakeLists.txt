# 1. Define the base engine
add_library(test_engine
    lib/engine.cpp
)

target_include_directories(test_engine
    PRIVATE
        include
)

# 2. Install the engine as a shared library
install(
    TARGETS test_engine
    LIBRARY DESTINATION lib
)
install(
    DIRECTORY
        include
    DESTINATION
        .
    FILES_MATCHING
        PATTERN
            "*.h"
)

# 3. Export the engine so games can use it
include(cmake/export_targets.cmake)
