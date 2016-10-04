//example for static variable
import java.io.*;

public class Employee2{
	//salary variable is a private static variable
	private static double salary;

	//DEPARTMEN is constant
	public static final String DEPARTMENT = "Development";
	public static void main(String args[]){
		salary = 1000;
		System.out.println(DEPARTMENT + "average salary:" + salary);
	}
}
