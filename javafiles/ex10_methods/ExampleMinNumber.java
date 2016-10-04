public class ExampleMinNumber{
	public static void main(String[] args){
		int a = 11;
		int b = 12;
		int c = minFunction(a,b);
		System.out.println("Minimum Value = " + c);
	}

	public static int minFunction(int n1, int n2){
		if (n1>n2) return n2;
		else return n1;
	}
}
