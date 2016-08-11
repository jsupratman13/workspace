%module example
%include "std_string.i"

%{
    #define SWIG_FILE_WITH_INIT
%}

%{
    #include "example.h"
%}

%include "example.h"
