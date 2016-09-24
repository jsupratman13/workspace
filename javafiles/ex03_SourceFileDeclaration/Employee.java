import java.io.*; //ask compiler to load all the classes available in directory java_installation/java/io

public class Employee{
	String name;
	int age;
	String designation;
	double salary;

	//this is the contructor
	public Employee(String name){
		this.name = name;
	}

	//assign the age
	public void empAge(int empAge){
		age = empAge;
	}

	//assign the designation to variable designation
	public void empDesignation(String empDesig){
		designation = empDesig;
	}

	//assign salary
	public void empSalary(double empSalary){
		salary = empSalary;
	}

	//print employee detail
	public void printEmployee(){
		System.out.println("Name: "+name);
		System.out.println("Age: "+ age);
		System.out.println("Designation: "+designation);
		System.out.println("Salary: "+salary);
	}
}


