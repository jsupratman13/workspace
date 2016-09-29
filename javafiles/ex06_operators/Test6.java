class Test{}

public class Test6 extends Test{
	public static void main(String args[]){
		String name = "James";
		//following will return true since name is type of string
		boolean result = name instanceof String;
		System.out.println(result);

		Test a = new Test6();
		result = a instanceof Test6;
		System.out.println(result);
	}
}
