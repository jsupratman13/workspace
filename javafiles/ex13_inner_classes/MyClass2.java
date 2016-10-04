class OuterDemo{
	//private variable
	private int num = 127;
	//inner class
	public class InnerDemo{
		public int getNum(){
			System.out.println("This is getNum method of the ineer class");
			return num;
		}
	}
}

public class MyClass2{
	public static void main(String[] args){
		//instantiating the outer class
		OuterDemo outer = new OuterDemo();
		//Instantiating the inner class
		OuterDemo.InnerDemo inner = outer.new InnerDemo();
		System.out.println(inner.getNum());
	}
}

