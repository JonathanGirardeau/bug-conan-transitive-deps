cmake_minimum_required(VERSION 3.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(dep)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(SOURCES
  code/src/dep/Dep.cpp
)

set(HEADERS
  code/src/dep/Dep.hpp
)

add_library(${PROJECT_NAME} ${SOURCES} ${HEADERS})

target_link_libraries(${PROJECT_NAME} PUBLIC CONAN_PKG::spdlog)

target_include_directories(${PROJECT_NAME} PRIVATE code/src/dep)
