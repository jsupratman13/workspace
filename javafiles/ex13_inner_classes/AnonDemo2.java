//interface
interface Message{
	String greet();
}

public class AnonDemo2{
	//method which accpets the objec of interface Message
	public void displayMessage(Message m){
		System.out.println(m.greet() + ", This is an example of anonymous inner class as an arguement");
	}

	public static void main(String[] args){
		AnonDemo2 obj = new AnonDemo2();

		obj.displayMessage(new Message(){
			public String greet(){
				return "Hello";
			}
		});
	}
}
