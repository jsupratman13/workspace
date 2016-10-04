class Calculation{
	int z;
	
	public void addition(int x, int y){
		z = x+y;
		System.out.println("the sum is " + z);
	}

	public void subtraction(int x, int y){
		z = x-y;
		System.out.println("the difference is " + z);
	}
}

public class MyCalculation extends Calculation{
	public void multiplication(int x, int y){
		z = x*y;
		System.out.println("the product is " + z);
	}

	public static void main(String[] args){
		int a = 20, b = 10;
		MyCalculation demo = new MyCalculation();
		demo.addition(a,b);
		demo.subtraction(a,b);
		demo.multiplication(a,b);
	}
}
