class Outer_Demo{
	int num;
	// inner class
	private class Inner_Demo{
		public void print(){
			System.out.println("This is an inner class");
		}
	}
	//Accessing the inner class from the method within
	void displayInner(){
		Inner_Demo inner = new Inner_Demo();
		inner.print();
	}
}

public class MyClass{
	public static void main(String[] args){
		//Instantiating the outer class
		Outer_Demo outer = new Outer_Demo();
		//Accessing the displayInner method
		outer.displayInner();
	}
}
