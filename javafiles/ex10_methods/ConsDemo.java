class MyClass{
	int x;

	//foloowing is the contsructor
	MyClass(int i){
		x = i;
	}
}
public class ConsDemo{
	public static void main(String[] args){
		MyClass t1 = new MyClass(10);
		MyClass t2 = new MyClass(20);
		System.out.println(t1.x + " " + t2.x);
	}
}
