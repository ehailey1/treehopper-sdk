cmake_minimum_required(VERSION 3.6)

add_definitions(-D_UNICODE)
add_definitions(-DUNICODE)

project(treehopper VERSION 0.1 LANGUAGES CXX)

include(GNUInstallDirs)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_subdirectory(API)

add_subdirectory(Demos/AnalogRead)
add_subdirectory(Demos/Blink)
add_subdirectory(Demos/DigitalIn)
add_subdirectory(Demos/I2cDeviceScanner)
add_subdirectory(Demos/Pwm)
add_subdirectory(Demos/Sandbox)

add_subdirectory(Demos/Libraries/RotaryEncoder)
add_subdirectory(Demos/Libraries/ImuDemo)
add_subdirectory(Demos/Libraries/Dm632)

