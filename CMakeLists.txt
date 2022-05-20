cmake_minimum_required (VERSION 3.5)

project (HelloWorld)

find_package( OpenCV REQUIRED )

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Werror -std=c++14")
set (source_dir "${PROJECT_SOURCE_DIR}/src/")

file (GLOB source_files "${source_dir}/*.cpp")
# add_subdirectory(${PROJECT_SOURCE_DIR}/src/opencv/)

include_directories( ${OpenCV_INCLUDE_DIRS} )

add_executable (HelloWorld ${source_files})
target_link_libraries( HelloWorld ${OpenCV_LIBS} )
