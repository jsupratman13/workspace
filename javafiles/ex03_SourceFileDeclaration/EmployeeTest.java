import java.io.*;

public class EmployeeTest{
	public static void main(String args[]){
		//create two boject using contructor
		Employee empOne = new Employee("Hilary Trump");
		Employee empTwo = new Employee("Donald Clinton");

		//invoke method fore each object
		empOne.empAge(26);
		empOne.empDesignation("Senior Software Engineer");
		empOne.empSalary(1000);
		empTwo.empAge(21);
		empTwo.empDesignation("Software Engineer");
		empTwo.empSalary(500);

		empOne.printEmployee();
		empTwo.printEmployee();
	}
}

