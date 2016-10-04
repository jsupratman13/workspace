#Inheritance
process where one class acquires the properties of another
##extend keyword
* used to inherit properties of class
```java
class Super{
...
}
class Sub extends Super{
...
}
```
* think of it as is-a relationship
```
class Animal{}
public class Dog extends Animal{}
```
* Dog is-a animal

##super keyword
similar to this keyword
* used to differentiate the members of superclass from member of sublcass
* used to invoke the superclass contructor from subclass
```java
super.variable;
super.method();
super(value); //invoking constructor
```
#Abstract
if you want a class to contain a particular method but the actual implmentation is determined by child class
* if method have abstract, class must be abstract

#Interface
* Similar to writing class but class describes the attributes and behaviors of an object while interface contains behaviors that a class implements
* unless class that implements interface is abstract, all methods needs to be defined in the class
```java
import java.lang.*;
public interface NameOfInterface{
	//any number of final, static fields
	//any number of abstract method declarations
}
```

#Packages
* mechanism to encapsulate a group of classes interfaces and sub packages
* organize files into one directories
* all java files should have them, one without them is only for temporary or prototype testing
* resuable, easy to locate, prevent name collision
* built in package like java.io (input output stream) java.lang () but we can make our own

##Define package
```
package tools;
public class Hammer{
	public void id(){
		...
	}
}
```
##How to use package
1. declaring the full name
```
com.package1.package2 name = new com.package1.package2();
```
However this is time consuming so therefore
2. using import
```
import com.package1.package2; //for one package
import com.package1.*; //for all package
class myClass{
	package2 name = new package2();
}
```

##Compiling packages
compiling sources must have packaging directories
```
package mypackage;
```
To compile and run
```java
javac -d [folder destination] [filename].java
java [folder destination].[filename]
```

##Set path
you can tell java to search through certain directories when executing stuff
```
set CLASSPATH=.;C:\[directories]
```

```
