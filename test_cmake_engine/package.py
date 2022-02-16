name = "test_cmake_engine"

version = "1.0.0"

description = "A base CMake project which just exports its C++ modules"

authors = ["ColinKennedy"]

private_build_requires = ["cmake-3.14+<4", "gcc-8.2+<9", "make-3.82+<4"]

build_system = "cmake"


def commands():
    import os

    env.CMAKE_PREFIX_PATH.append(os.path.join(root, "lib", "cmake", "test_engine"))
    env.CPP_INCLUDE_PATH.append(os.path.join(root, "include"))
    env.LD_LIBRARY_PATH.append(os.path.join(root, "lib"))
    env.LIBRARY_PATH.append(os.path.join(root, "lib"))
