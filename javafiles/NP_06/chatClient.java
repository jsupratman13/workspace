/**
 * chat client
 * chatClient.java
 *
 * example how to use
 * java chatClient 192.168.1.1
 */
import java.io.*;
import java.net.*;

public class chatClient{
    static final int CHAT_PORT = 12345;//chat port number
    Socket sock;             //connection socket
    BufferedInputStream in;  //input stream
    BufferedOutputStream out;//output steam
    String host;             //server address
    int port;                //server port

    //Constructor overload 2
    public chatClient(String host, int port)
      throws IOException,UnknownHostException
    {
        this.host = host;
        this.port = port;
        sock = new Socket(host, port);
        out = new BufferedOutputStream(sock.getOutputStream());
        in = new BufferedInputStream(sock.getInputStream());

    }
    //Constructor overload 1
    public chatClient(String host) throws IOException
    {
        this(host, CHAT_PORT);
    }
    //chat process
    public void chatProc() throws IOException
    {
        try{
            //SendInHandler,AGetOutHandler object create
            SendInHandler insto = new SendInHandler(System.in,out);
            GetOutHandler outst = new GetOutHandler(in,System.out);
            //create thread
            Thread th1 = new Thread(insto);
            Thread th2 = new Thread(outst);
            //activate thread
            th1.start();
            th2.start();
        }
        catch(Exception e){
            System.err.println(e);
            System.exit(1);
        }
    }
    //main process
    public static void main(String[] args){
        try{
            if(args.length != 1){
               throw new IllegalArgumentException("usage:>java chatClient <host_address>");
            }
            chatClient chat = new chatClient(args[0]);
            chat.chatProc();
        }catch(Exception e){
            e.printStackTrace();
            System.exit(1);
        }
    }
}
//input transmission handler process
class SendInHandler implements Runnable{
    static final int LEN = 1024;    //keyinbuf size
    byte[] keyinbuf = new byte[LEN];//transmission buffer
    int k;                  //byte number
    InputStream in = null;  //define input stream
    OutputStream out = null;//define output steam
    //constructor
    public SendInHandler(InputStream in, OutputStream out)
      throws IOException
    {
        this.in = in;
        this.out = out;
    }
    //quit check
    private void quitCheck(byte buf[], int count) throws IOException{
        String keyinstr = new String(buf,0,count);
        if(keyinstr.equals("quit\r\n") || keyinstr.equals("QUIT\r\n")) {
            System.out.println("please disconnect " + "(enter [Ctrl]+[C])");
        }
    }
    //transmit stream data
    public void run(){
        while(true){
            try{
                //read data key
                k = in.read(keyinbuf);
                if(k == -1){
                    break;
                }
                //write stream transmission data
                out.write(keyinbuf, 0, k);
                //flust stream data
                out.flush();
                quitCheck(keyinbuf, k);
            }catch(Exception e){
                e.printStackTrace();
                System.exit(1);
            }
        }
    }
}
//Receiver output handler process
class GetOutHandler implements Runnable{
    static final int LEN = 1024;//getbuf size
    byte[] getbuf = new byte[LEN];//receiver buffer
    int k;                  //byte number
    InputStream in = null;  //define input stream
    OutputStream out = null;//define output stream
    //constructor
    public GetOutHandler(InputStream in, OutputStream out)
      throws IOException
    {
        this.in = in;
        this.out = out;
    }
    //stream receive data
    public void run(){
        while(true){
            try{
                //read receive data
                k = in.read(getbuf);
                if(k == -1){
                    break;
                }
                //write stream transmission data
                out.write(getbuf, 0, k);
                //flush stream data
                out.flush();
            }catch(Exception e){
                e.printStackTrace();
                System.exit(1);
            }
        }
    }
}
