public class Test{
	public static void main(String args[]){
		Integer x = 5; // box from int to Integer object
		System.out.println(x.byteValue());
		System.out.println(x.doubleValue());
		x = x + 19; //unboxing
	}
}
