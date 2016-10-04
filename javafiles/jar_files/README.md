#Jar
Combine all files into one
```
javac [filename].java
echo Main-Class: [start class] > manifest.txt
jar cvfm [start class].jar manifest.txt [filename].class
java -jar [start class].jar
```

