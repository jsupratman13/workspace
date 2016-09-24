#Classes and Object in Java

##Compile Method
javac Singleton.java SingletonDemo.java

##sample class
```java
public class Dog{
	String breed;
	int age;
	String color;

	void barking(){}
	void hungry(){}
	void sleeping(){}
}
```
##Variable type
* Local variable: define inside method, constructors or blocks
* Instance variable: define inside class but outside method
* Class variable: define within class outside any method with static keyword

##Contructors
same as c++. constructor is mandatory and java will automatically make one if not included
```java
public class Pupply{
	public Puppy(){
	}
	public Puppy(String name){
		// This constructor has one parameter, name.
	}
}
```

##Singleton Class
Control object creation to one only.
```java
public class ClassicSingleton{
	private static ClassicSingleton instance = null;
	private ClassicSingleton(){
		//Exists only to defeat intantiation
	}

	public static ClassicSingleton getInstance()[
		if(instance == null){
			instance = new ClassSingleton();
		}
		return instance;
	}
}
```
* sample above emply technique known as lazy instantiation, singleton instance is not created until getInstance(9 method is called for first time -> ensures that singleton instance are created only when needed

##Accessing instance variable and methods
Examples are 
```java
//First create an object
ObjectReference = new Constructor();

//call on variable
ObjectReference.variableName;

//call on method
ObjectReference.MethodName();
```


