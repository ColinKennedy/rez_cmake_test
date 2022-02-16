project(test_cmake_project LANGUAGES CXX)

find_package(TestEngine CONFIG REQUIRED)

add_subdirectory(src)
