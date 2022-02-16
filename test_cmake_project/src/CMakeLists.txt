add_executable(run_it
    main.cpp
)

target_link_libraries(run_it
    PUBLIC
        test_engine::test_engine
)

install(TARGETS run_it DESTINATION bin)
