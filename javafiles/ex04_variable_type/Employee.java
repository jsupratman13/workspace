//example for instance variable
import java.io.*;

public class Employee{
	//instance variable visible for any child class
	public String name;

	//instance variable visible in this class only
	private double salary;

	public Employee(String empName){
		name = empName;
	}

	public void setSalary(double empSal){
		salary = empSal;
	}

	public void printEmp(){
		System.out.println("name:" + name);
		System.out.println("salary:"+ salary);
	}

	public static void main(String args[]){
		Employee empOne = new Employee("Osama");
		empOne.setSalary(1000);
		empOne.printEmp();
	}
}

