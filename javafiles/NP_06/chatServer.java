/**
 * Chat server
 * chatServer.java
 * 
 * example
 * java chatServer
 */
import java.io.*;
import java.net.*;
import java.util.*;

public class chatServer{
    static final int CHAT_PORT = 12345;//port number
    static ServerSocket servsock;      //define server socket
    static ArrayList al;               //define arraylist

    //transmit message
    public static void sendMess(String mess){
        Socket sockdt;//define socket
        BufferedWriter wr; //output stream usage
        int total;//total socket
        int num = 0;//socket number
        num = al.size();
        total = num;
        //System.out.println(num);
        //confirm socket
        if(num != 0){
            for(int i=0;i<total;i++){
                //get socket
                sockdt = (Socket)al.get(i);
                try{
                    OutputStream out = sockdt.getOutputStream();
                    wr = new BufferedWriter(new OutputStreamWriter(out));
                    //output socket message
                    wr.write(mess,0,mess.length());
                    wr.flush();
                }catch (IOException ex){}
            }
        }
        System.out.println(mess);
    }
    //append socket information
    public static void addEntry(Socket s){
        if (al == null){ //if no socket..
            al = new ArrayList(); //create socket
        }
        al.add(s); //append client socket
        //System.out.println(al);
    }
    //delete socket information
    public static void deleteEntry(Socket s){
        if(al.isEmpty() != true){ //if there is socket
            al.remove(s); //delete socket
        }
        //System.out.println(al);
    }
    //main process
    public static void main(String[] args){
        try{
            //generate socket server
            servsock = new ServerSocket(CHAT_PORT);
        }catch (IOException e){
            System.err.println("creation error");
            System.exit(1);
        }
        System.out.println("Connections on port " 
                     + servsock.getLocalPort());
        //infinite loop
        while(true){
            try{
                //accept connection
                Socket sock = servsock.accept();
                addEntry(sock);
                clientProc cp = new clientProc(sock);
                //generate instance for thread
                Thread th = new Thread(cp);
                //activate thread
                th.start();
            }catch (IOException e){
                System.err.println("accept error.");
                System.exit(1);
            }
        }
    }
}

//client process
class clientProc implements Runnable{
    Socket s;           //for socket
    BufferedReader rd;  //for input stream
    BufferedWriter wr;  //for output stream
    String name = null; //login name
    boolean bflg =true; //quit flag
    //constructor
    public clientProc(Socket s) throws IOException{
        this.s = s;
        //define input stream
        InputStream in = s.getInputStream();
        rd = new BufferedReader(new InputStreamReader(in));
        OutputStream out = s.getOutputStream();
        wr = new BufferedWriter(new OutputStreamWriter(out));
    }
    //thread main process
    public void run(){
        try{
            String sendstr = "Handle name";
            wr.write(sendstr,0,sendstr.length());
            wr.flush();
            while(name  == null){
                name = rd.readLine();//login name
            }
            //login message
            chatServer.sendMess("#"+name+" has entered\r\n");
            String mess = rd.readLine(); //message list
            if("quit".equalsIgnoreCase(mess)){//quit?
                bflg = false;
            }
            while(bflg){
                //transmit message to all of client
                chatServer.sendMess(name + ">" +mess + "\r\n");
                mess = rd.readLine(); //message list
                if("quit".equalsIgnoreCase(mess)){//quit?
                    bflg = false;
                }
            }
            //logout message
            chatServer.sendMess("#"+name+" has left\r\n");
            chatServer.deleteEntry(s);
            s.close();
        }catch (IOException e){
            e.printStackTrace();
            try{
                s.close();
                System.err.println("running error");
                System.exit(1);
            }catch (IOException e1){
            }
        }
    }
}
