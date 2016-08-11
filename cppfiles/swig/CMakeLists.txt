find_package(PythonLibs REQUIRED)
find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})
include(GenerateExportHeader)

include_directories(
	${CMAKE_CURRENT_SOURCE_DIR}
	${POJECT_BINARY_DIR}
	${PYTHON_INCLUDE_PATH}
)

set(EXAM_SRCS
	example.h
)

set(INTERFACE_FILES
	example.i
)

set_source_files_properties(${INTERFACE_FILES} PROPERTIES CPLUSPLUS ON)
swig_add_module(example python ${INTERFACE_FILES}
	${EXAM_SRCS}
)

swig_link_libraries(example
	${PYTHON_LIBRARIES}
)
