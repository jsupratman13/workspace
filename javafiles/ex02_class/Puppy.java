public class Puppy{
	
	//instance variable
	int puppyAge;

	//This constructor has one parameter
	public Puppy(String name){
		System.out.println("Passed name is: " + name);
	}

	public void setAge(int age){
		puppyAge = age;
	}

	public int getAge(){
		System.out.println("Puppy's age is: " + puppyAge);
		return puppyAge;
	}

	public static void main(String[] args){
		//object creation
		Puppy myPuppy = new Puppy("tommy");

		//call class method to set puppy age
		myPuppy.setAge(2);

		//call method to get puppy age
		myPuppy.getAge();

		//can access instance variable as well
		System.out.println("Variable value: " + myPuppy.puppyAge);

	}
}
