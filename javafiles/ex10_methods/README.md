# Methods
* modifier: define access type of method
* returnType: method may return value
* nameOfMethod: method name
* parameter list: list of parameter
* method body: what the method does
```java
modifier returnType nameOfMethod(parameter list){
	...method body...
}
```

## Void keyword
* special type of returnType that does not return anything

## Overloading
* method with same name but different parameter

# Constructor
* initialization of method. made default is made if none are made

## this keyword
this keyword is used as reference to the object of the current class
* differentiate the instance variables from local variables if they have same names within contructor or method
```java
class Student{
	int age;
	Student(int age){
	this.age=age;
	}
}
```
* call one type of constructor form other in a class. aka explicit constructor invocation
```java
class Student{
	int age;
	Student(){
		this(20);
	}
	Student(int age){
		this.age=age;
	}
```

## Variable argurments
java allows passing variable number of arguments of the same type to a method
```java
typeName... parameterName
```

## Finalize method
* use method called finalize() to be called just be object's final destruction
```java
protected void finalize(){
	//code
}
```

