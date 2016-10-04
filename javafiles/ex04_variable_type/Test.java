//example for local variable
public class Test{
	public void pupAge(){
		int age = 0; // need to initialize with value
		age = age + 7;
		System.out.println("puppy age is: "+ age);
	}

	public static void main(String args[]){
		Test test = new Test();
		test.pupAge();
	}
}
