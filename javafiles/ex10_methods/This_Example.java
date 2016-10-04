public class This_Example{
	//Stnaces of variable
	int num=10;
	
	This_Example(){
		System.out.println("This is an example program on keyword this ");
	}
	
	This_Example(int num){
		//Invoke the default constructor
		this();

		//assigining the local variable num to the instance variable num
		this.num = num;
	}

	public void greet(){
		System.out.println("Hello world!");
	}

	public void print(){
		//local variable num
		int num = 20;

		//printing the local variable
		System.out.println("value of local variable num is: " + num);

		//printing the instance variable
		System.out.println("value of instance variable is: " + this.num);

		//Invoking the greet method
		this.greet();
	}

	public static void main(String[] args){
		//Instatiating the class
		This_Example obj1 = new This_Example();

		//invoking the print method
		obj1.print();

		//Passing a new value to the num variable through parametrized constructor
		This_Example obj2 = new This_Example(30);

		//invoking the print method
		obj2.print();
	}
}

