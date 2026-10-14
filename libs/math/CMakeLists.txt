set(INCLUDE_ROOT "${PROJECT_SOURCE_DIR}/include/plank/math")

target_sources(plank
    PRIVATE
        ${INCLUDE_ROOT}/vector.hpp
)
