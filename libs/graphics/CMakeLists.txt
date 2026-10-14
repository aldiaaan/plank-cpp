set(INCLUDE_ROOT "${PROJECT_SOURCE_DIR}/include/plank/graphics")

target_sources(plank
    PRIVATE
        ${INCLUDE_ROOT}/renderer.hpp
        renderer.cpp
)
