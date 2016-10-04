#Java Files
Java program exercise. Require JDK

##Compile Method
javac [filename].java (filename must be same as class name)
java [filename]

##Include external JAR files
javac -cp .:path1/xxx.jar:path2/yyy.jar [filename].java
java -cp .:path1/xxx.jar:path2/yyy.jar [filename]

##Include Externa Native Libraries
* .lib = windows static library
* .dll = windows dynamically link library
* .a = unix static library
* .so = unix shared library
java -Djava.library.path=xxx [filename]

##View jar files
jar -tvf [filename].jar

##Characteristic
* object oriented
* platfrom independent
* simple
* secure
* architecture-neutral
* portable
* robust
* multithreaded
* interpreted
* high performance
* distributed
* dynamic


