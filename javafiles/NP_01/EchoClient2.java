import	java.net.Socket;
import	java.net.ServerSocket;
import	java.io.BufferedReader;
import	java.io.InputStreamReader;
import	java.io.PrintWriter;
import	java.io.IOException;

public class EchoClient2 {
	public static final int ECHO_PORT = 10007;

	public static void main(String[] args) {
		Socket socket = null;

		try {
			if (args.length != 0) {
				socket = new Socket(args[0], ECHO_PORT);
			} else {
				System.out.println("connect to localhost");
				socket = new Socket("localhost", ECHO_PORT);
			}
			System.out.println("connected=" + socket.getRemoteSocketAddress());
			BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
			PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
			BufferedReader keyIn = new BufferedReader(new InputStreamReader(System.in));
			String input;
			while ((input = keyIn.readLine()).length() > 0) {
				out.println(input);
				String line = in.readLine();
				if (line != null) {
					System.out.println(line);
				} else {
					break;
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (socket != null) {
					socket.close();
				}
			} catch (IOException e) {}
			System.out.println("disconnected " + socket.getRemoteSocketAddress());
		}
	}
}
