import java.net.Socket;
import java.net.ServerSocket;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.IOException;

public class SumupServer {

    public static final int SUMUP_PORT = 12345;

    public static void main(String args[]) {
        ServerSocket serverSocket = null;
        try {
            serverSocket = new ServerSocket(SUMUP_PORT);
            System.out.println("Activate SumupServer(port="
                               + serverSocket.getLocalPort() + ")");
            while (true) {
                Socket socket = serverSocket.accept();
                new SumupThread(socket).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (serverSocket != null) {
                    serverSocket.close();
                }
            } catch (IOException e) {}
        }
    }

}

class SumupThread extends Thread {

    private Socket socket;
    private int sum;

    public SumupThread(Socket socket) {
        this.socket = socket;
        System.out.println("Connected to "
                           + socket.getRemoteSocketAddress());
    }

    public void run() {
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(
)));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            String line;
            while ( (line = in.readLine()) != null ) {
                System.out.println(socket.getRemoteSocketAddress()
                                   + " Recevied: " + line);
                sum += Integer.parseInt(line);
                out.println(Integer.toString(sum));
				//out.println(line);
                System.out.println(socket.getRemoteSocketAddress()
                                   + " Send: " + sum);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (socket != null) {
                    socket.close();
                }
            } catch (IOException e) {}
            System.out.println("Disconnected "
                               + socket.getRemoteSocketAddress());
        }
    }

}
