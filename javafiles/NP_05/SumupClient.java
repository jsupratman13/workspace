import java.net.Socket;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.IOException;

public class SumupClient {

    public static final int SUMUP_PORT = 12345;

    public static void main(String args[]) {
        Socket socket = null;
        try {
            socket = new Socket(args[0], SUMUP_PORT);
            System.out.println("Connected "
                               + socket.getRemoteSocketAddress());
            BufferedReader recIn = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader keyIn = new BufferedReader(new InputStreamReader(System.in));
            String message;
            while ( ( message = keyIn.readLine()).length() > 0 ) {
                out.println(message);
                String line = recIn.readLine();
                if (line != null) {
                    System.out.println("Sum: " + line);
                } else {
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (socket != null) {
                    System.out.println("Disconnected "
                                       + socket.getRemoteSocketAddress());
                    socket.close();
                }
            } catch (IOException e) {}
        }
    }

}
