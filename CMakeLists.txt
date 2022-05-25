cmake_minimum_required (VERSION 3.5)

project (HelloWorld)

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable (Contours src/Contours.cpp)
add_executable (Main src/Main.cpp)

target_link_libraries(Contours ${OpenCV_LIBS} )
target_link_libraries(Main ${OpenCV_LIBS} )

