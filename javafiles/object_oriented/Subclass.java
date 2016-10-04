class Superclass{
	int age;

	Superclass(int age){
		this.age = age;
	}

	public void getAge(){
		System.out.println("value in superclass: " + age);
	}
}

public class Subclass extends Superclass{
	Subclass(int age){
		super(age);
	}

	public static void main(String[] args){
		Subclass s = new Subclass(24);
		s.getAge();
	}
}
