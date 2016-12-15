import java.net.Socket;
import java.net.ServerSocket;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.IOException;

public class MultiEchoServer {
  public static final int ECHO_PORT = 10007;

  public static void main(String[] args) {
    ServerSocket serverSocket = null;
    Socket socket = null;
    try {
      serverSocket = new ServerSocket(ECHO_PORT);
      System.out.println("Activate EchoServer(port=" +
                     serverSocket.getLocalPort() + ")");
      while (true) {
        socket = serverSocket.accept();
        new EchoThread(socket).run();	//create EchoThread for each socket to run
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

class EchoThread extends Thread {

  private Socket socket;

  public EchoThread(Socket socket) {
    this.socket = socket;
    System.out.println("Connected to " +
                       socket.getRemoteSocketAddress());
  }

  public void run() {
    try {
      // Same as EchoServer
      BufferedReader in = new BufferedReader(
        new InputStreamReader(socket.getInputStream()));
      PrintWriter out =
        new PrintWriter(socket.getOutputStream(), true);
      String line;
      while ( (line = in.readLine()) != null ) {
        System.out.println(socket.getRemoteSocketAddress() + " Received: " + line);
        out.println(line);
        System.out.println(socket.getRemoteSocketAddress() + " Send: " + line);
      }
    } catch (IOException e) {
      // exceptional processing
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
