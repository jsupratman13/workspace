// java enums predefine values -> prevent bugs, prevent non define variable
class FreshJuice{
	enum FreshJuiceSize{ SMALL, MEDIUM, LARGE}
	FreshJuiceSize size;
}

public class FreshJuiceTest{
	public static void main(String args[]){
		FreshJuice juice = new FreshJuice();
		juice.size = FreshJuice.FreshJuiceSize.MEDIUM;
		System.out.println("Size: "+ juice.size);
	}
}
