#innter class
class within class is called nested class

```java
class Outer_Demo{
	class Nested_Demo{
	}
}
```
two types
* static nested class
* non-static nested class
  * inner classes
  * method local inner classes
  * anonymous inner class

##anonymous inner class
used to override the method of a class or an interface
```java
AnonymousInner anInner = new AnonymousInner(){
	public void myMethod(){
	....
	}
};
```
##anonymous inner class as argument
```java
obj.myMethod(new MyClass(){
	public void Do(){
	...
	}
});
```


