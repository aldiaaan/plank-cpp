set(INCLUDE_ROOT "${PROJECT_SOURCE_DIR}/include/plank/Graphics")

target_sources(plank
    PRIVATE
        ${INCLUDE_ROOT}/Renderer.hpp
        Renderer.cpp
)
