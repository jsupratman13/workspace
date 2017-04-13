## Source File Declaration Rule
Rules for declaring classes, import statements and package statements in a source file
* Only one public class per source file
* Source file can have multiple non-public classes
* public class name should be the name of the source file appended by java. ex public class Dog {} then Dog.java
* if class is define inside a package, package statment should be first statement in source file
* if import statement are present, must be written between package statement and class declration
* import and package statements will imply to all classes present in the source file. it is not possible to declare different import/package statements to different classes in the source file

## Java Packages
A way of catogrizing the classes and interfaces. Makes it easier when developing applications in Java which included hundred of classes and interface

## Import Statements
If a fully qualified name, including the package and the class name, is given, then compiler can easily locate source code or classes. Import statement is a way of giving the proper location for the compiler to find the particular class.

