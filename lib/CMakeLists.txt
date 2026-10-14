add_library(plank STATIC "")
add_library(plank::plank ALIAS plank)

target_include_directories(
  plank
  PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include/plank>)

set_target_properties(plank PROPERTIES LINKER_LANGUAGE CXX)

add_subdirectory(Math)
add_subdirectory(Graphics)
