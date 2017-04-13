# Array
Same as c with feature but with extra features

## declaration
```java
datatype[] arrayRefVar; //preferred way
datatype arrayRefvar[]; //works but not preferred
```

## new aray
```java
arrayRefVar = new datatype[arraysize]; //make sure arrayRefVar is defined
dataType[] arrayVar = {value1, value2, ... valueN};
```
## Loops
can be used in loops
```java
arrayRefVar = {v1, v2 ...};
for(int value: arrRefVar){
...
}
```

## Method
* can insert array to method
```java
public static void printArray(int[] array){
	...
}
```
* can return array from method
```java
public static int[] reverse(int[] list){
	int[] result = new int[list.length];
	...
	return result;
}
```



