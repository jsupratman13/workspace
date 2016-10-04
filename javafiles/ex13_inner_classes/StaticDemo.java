public class StaticDemo{
	static class NestedDemo{
		public void myMethod(){
			System.out.println("This is my nested class");
		}
	}

	public static void main(String[] argts){
		StaticDemo.NestedDemo nested = new StaticDemo.NestedDemo();
		nested.myMethod();
	}
}
