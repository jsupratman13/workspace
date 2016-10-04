import java.io.File;
import java.io.FileReader;

public class FilenotFound_Demo{
	public static void main(String[] args){
		File file = new File("jjaja.txt");
		FileReader fr = new FileReader(file);
	}
}
