public class OuterClass{
	//instance method of the outer class
	void myMethod(){
		final int num = 23;

		//method -local inner class
		class MethodInnerDemo{
			public void print(){
				System.out.println("this is method inner class " + num);
			}
		}

		//access the inner class
		MethodInnerDemo inner = new MethodInnerDemo();
		inner.print();
	}
	
	public static void main(String[] args){
		OuterClass outer = new OuterClass();
		outer.myMethod();
	}
}

