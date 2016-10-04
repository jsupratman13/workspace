abstract class AnonymousInner{
	public abstract void myMethod();
}

public class AnonDemo{
	public static void main(String[] args){
		AnonymousInner inner = new AnonymousInner(){
			public void myMethod(){
				System.out.println("This is an example of anonymous inner class");
			}
		};
		inner.myMethod();
	}
}
