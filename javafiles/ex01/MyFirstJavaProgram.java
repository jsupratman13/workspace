import java.util.*;
public class MyFirstJavaProgram{
	//print hello world
	public static void main(String []args){
        Integer[] lis = new Integer[] {1,2,3,4};
		System.out.println("Hello World");
        System.out.println(Arrays.toString(lis));
        Collections.shuffle(Arrays.asList(lis));
        System.out.println(Arrays.toString(lis));
        System.out.println(lis[2]);
        System.out.println(Math.round(41.1233*10.0)/10.0);
	}
}
