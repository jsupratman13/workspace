import java.io.*;

public class FileRead{
	public static void main(String[] args) throws IOException{
		File file = new File("Hello.txt");
		//creates the file
		file.createNewFile();
		//creates a file writer object
		FileWriter writer = new FileWriter(file);
		//writes the content to the file
		writer.write("This\n is\n an\n example\n");
		writer.flush();
		writer.close();

		//crates a file reader object
		FileReader reader = new FileReader(file);
		char[]  a = new char[50];
		reader.read(a); //read content to the array
		for(char c:a){
			System.out.print(c); //prints the charcter one by one
		}
		reader.close();
	}
}
