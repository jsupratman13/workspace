# C++ class
In C++ classes are what makes C++ object oriented programming language.
Classes are made like this:
```c++
class ClassName(){...
...
};
```
## Compile Method
g++ [filename]

# Content
1. class
2. inheritance
3. constructor
4. friend
5. class pointer
6. class static
7. polymorphism
8. abstract/encapsulation
9. overload
10. interface

## Membership
In C++, class have 3 common member, public, protected and private.
In each member have their own special access.

access|public|protected|private
------|------|---------|-------
same class|yes|yes|yes
derived class|yes|yes|no
outside class|yes|no|no

Normally public membership is used for interface such as accessing function.
Normally private/protected membership is used for implementing data and variable.

## Access
To access member of class use dot.
```c++
ClassName classname;
classname.function();
```
To access member of class through pointer use arrow.
```c++
ClassName *classname;
classname->function();
```
