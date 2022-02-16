## How To Build
1. Create `cmake`, `gcc`, and `make` Rez packages locally
2. Run this

```sh
(cd test_cmake_engine && rez-build -ci)
(cd test_cmake_project && rez-build -ci)
```

## Testing It
```sh
rez-env test_cmake_project -- run_it
```

Should print out "Doing something!"
