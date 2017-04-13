# CMake exercise
CMake is a automatic software building tool. Different system uses different tools to compile their program such as Windows with Visual Studio and Linux with make. Each system has its own library and environment which requires setup. For example, program using OpenGL and OpenCV requires library name and header file location during compilation which might be difficult for beginners (like me!). Therefore CMake there make things easier for setting up.
 ``
 write once, compile everywhere
 ```
it the idea

## Setup
* need CMakeLists.txt along with programs you want to build

## Build
```
cmake .
make
```

## Change build option
```
ccmake .
```

## Function
* set minimum version of CMake
```
cmake_minimum_required(VERSION XX)
```
* name the project
```
project(project_name)
```
* add executable files
```
add_executable(execute filename)
```

