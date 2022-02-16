name = "test_cmake_project"

version = "1.0.0"

description = "A base CMake project which just exports its C++ modules"

authors = ["ColinKennedy"]

private_build_requires = [
    "cmake-3.14+<4",
    "gcc-8.2+<9",
    "make-3.82+<4",
    "test_cmake_engine-1+<2",
]

build_system = "cmake"


def commands():
    import os

    env.PATH.append(os.path.join(root, "bin"))
