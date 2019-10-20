# For more information about using CMake with Android Studio, read the
# documentation: https://d.android.com/studio/projects/add-native-code.html

# Sets the minimum version of CMake required to build the native library.

cmake_minimum_required(VERSION 3.4.1)

AUX_SOURCE_DIRECTORY(src/main/cpp SRC_LIST)

add_library( # Sets the name of the library.
             native-code

             # Sets the library as a shared library.
             SHARED

             # Provides a relative path to your source file(s).
             ${SRC_LIST} )

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=address")
set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -fsanitize=address")

target_link_libraries( # Specifies the target library.
                       native-code

                       # Links the target library to the log library
                       # included in the NDK.
                       log)