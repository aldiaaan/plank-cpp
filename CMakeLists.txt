cmake_minimum_required(VERSION 3.20)

include(FetchContent)

# set(VCPKG_DISABLE_METRICS ON CACHE BOOL "Disable vcpkg metrics" FORCE)
# set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

project(
    plank
    VERSION "0.0.1"
    DESCRIPTION "Plank - Boilerplate for making CXX application"
    LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 23)

option(PLANK_BUILD_UNIT_TESTS "whether to build unit tests" OFF)

if(NOT PLANK_PLATFORM)
  if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set(CMAKE_CXX_STANDARD 23)
    set(PLANK_PLATFORM "MACOS")

    if(${CMAKE_SYSTEM_PROCESSOR} MATCHES "arm64")
      set(PLANK_ARCH "ARM64")
    else()
      set(PLANK_ARCH "X86_64")
    endif()
  elseif(${CMAKE_SYSTEM_NAME} MATCHES "Windows")
    set(PLANK_PLATFORM "WIN32")
    set(PLANK_ARCH "X86_64")
  elseif(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    set(PLANK_PLATFORM "LINUX")
    set(PLANK_ARCH "X86_64")
  else()
    message(FATAL_ERROR "Unsupported platform: ${CMAKE_SYSTEM_NAME}")
  endif()
endif()

FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG v1.18.0)
FetchContent_GetProperties(googletest)

add_subdirectory(lib)
add_subdirectory(src)

if(PLANK_BUILD_UNIT_TESTS)
    enable_testing()
    include(CTest)

    add_subdirectory(tests)
endif()
