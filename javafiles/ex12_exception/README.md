# Exceptions
there are three catagories of exceptions
* checked exceptions: occurs at compile time
* unchecked exceptions: occurs at execution
* errors: not exception but problem that arises beyond the control of user or programmer. ex stack overflow

## Catching exceptions
method of catching exception is through use of try and catch
```java
try{
	//protected code
}catch(ExceptionName e1){
	//catch block
}
```
* when using try, and with catch or finally
* multiple catch is possible

## Throws/Throw keyworld
* if method does not handle checked exception, method must declare using throw keyword
* throws is used to postpone the the handleing of checked exception
* throw is used to invoke an exception explicitly
```java
import java.io.*;
public class className{
	public void deposit(double amount) throws RemoteException
	{
		//Method implementation
		throw new RemoteException();
	}
	//Remainder of class definition
}
```

## finally block
* follows try or catch block. always execute regardless of an exception
* when using resources like streams, connections, we close them explicitly using finally block
```java
try{
	...
}catch(exception e1){
	...
}finally{
	...
}
```

## self made exception
Self made exception can be made
```java
class MyExcetpion extends Exception{
}
