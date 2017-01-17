// ｢海ゲーム｣GUI クライアントプログラムUmiAI.java
// このプログラムは,海ゲームのクライアントAIプログラムです
// 使い方java UmiAI
// 起動してloginボタンを押すと,接続先サーバの名前や利用者の名前を問い合わせてきます
// サーバ名と利用者名を入力してください
// 続いてOK ボタンを押すと,ポート番号10000 番でサーバと接続します
//
// プログラムを停止するにはlogout ボタンを押してください

// ライブラリの利用
import java.awt.*;// グラフィックス
import java.awt.event.*;// イベント関連
import java.awt.geom.*;
import java.net.*;// ネットワーク関連
import java.io.*;
import java.util.*;

// UmiAIクラス
// UmiAIプログラムの中心となるクラスです
public class UmiAI implements Runnable {
    Frame f;// クライアント情報表示用ウィンドウ
    Panel p;// 上下左右の移動ボタンと海の状態を表示するパネル
    Canvas c;// 海の状態を表示するキャンバス

    Hashtable fuelList = new Hashtable();
    Point2D.Double destination = new Point2D.Double(-1,-1);
    Point2D.Double fuelpos;
    Point2D.Double selfpos;
    int[][] delta = {{-1,0},{0,-1},{1,0},{0,1}};
    String[] move = {"left","down","right","up"};
    ArrayList path = new ArrayList();

    // コンストラクタ
    // GUI 画面の初期配置を行います
    public UmiAI ()
    {
        selfpos = new Point2D.Double(10,10);
        Button b;
        f = new Frame();//クライアント情報ウィンドウ全体の表示
        p = new Panel();//海表示部分と操作ボタンの表示
        p.setLayout(new BorderLayout());

        // upボタンの作成
        b = new Button("up");
        b.addActionListener(new ActionListener(){
            // upボタンが押されたらupコマンドを送信します
            public void actionPerformed(ActionEvent e){
                sendCommand("up");
            }
        });
        p.add(b, BorderLayout.NORTH);

        // leftボタンの作成
        b = new Button("left");
        b.addActionListener(new ActionListener(){
            // leftボタンが押されたらleftコマンドを送信します
            public void actionPerformed(ActionEvent e){
                sendCommand("left");
            }
        });
        p.add(b, BorderLayout.WEST);

        // rightボタンの作成
        b = new Button("right");
        b.addActionListener(new ActionListener(){
            // rightボタンが押されたらrightコマンドを送信します
            public void actionPerformed(ActionEvent e){
                sendCommand("right");
            }
        });
        p.add(b, BorderLayout.EAST);

        // downボタンの作成
        b = new Button("down");
        b.addActionListener(new ActionListener(){
            // downボタンが押されたらdownコマンドを送信します
            public void actionPerformed(ActionEvent e){
                sendCommand("down");
            }
        });
        p.add(b, BorderLayout.SOUTH);

        // 海上の様子を表示するCanvasを作成します
        c = new Canvas();
        c.setSize(256,256);// 大きさの設定
        // フレームに必要な部品を取り付けます
        p.add(c);
        f.add(p);

        // フレームfにloginボタンを取り付けます
        b = new Button("login");
        b.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                // loginボタンが押された場合の処理
                // サーバがセットされていなければlogin処理を行います
                if(server == null) login();
            }
        });
        f.add(b,BorderLayout.NORTH);

        // フレームfにlogoutボタンを取り付けます
        b = new Button("logout");
        b.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                logout();
            }
        });
        f.add(b,BorderLayout.SOUTH);

        // フレームfを表示します
        f.setSize(335,345);
        f.show();
    }

    // runメソッド
    // 500ミリ秒ごとに画面を更新します
    public void run(){
        while (true){
            try {
                Thread.sleep(100);
            }catch(Exception e){
            }
            // repainメソッドを用いて,サーバ上の情報を画面に出力します
            repaint();
        }
    }

    // login処理関連のオブジェクト
    int sx = 100;
    int sy = 100;
    TextField host, tf_name;
    Dialog d;

    // loginメソッド
    // loginウィンドウを表示し,必要な情報を得ます
    // 実際のlogin処理は,realLoginメソッドで行います
    void login(){
        // ウィンドウの表示とデータの入力
        d = new Dialog(f, true);
        host = new TextField(10) ;
        tf_name = new TextField(10) ;
        d.setLayout(new GridLayout(3,2));
        d.add(new Label("host:"));
        d.add(host);
        d.add(new Label("name:"));
        d.add(tf_name);
        Button b = new Button("OK");
        b.addActionListener(new ActionListener(){
     // 入力が完了したら,readlLoginメソッドを使ってサーバにloginします
            public void actionPerformed(ActionEvent e){
                realLogin(host.getText(), tf_name.getText());
                d.dispose();
            }
        });
        d.add(b);
        d.setResizable(true);
        d.setSize(200, 150);
        d.show();
        (new Thread(this)).start();
    }

    // realLogin関連のオブジェクト
    Socket server;// ゲームサーバとの接続ソケット
    int port = 10000;// 接続ポート
    BufferedReader in;// 入力ストリーム
    PrintWriter out;// 出力ストリーム
    String name;// ゲーム参加者の名前

    // realLoginメソッド
    // サーバへのlogin処理を行います
    void realLogin(String host, String name){
        try {
            // サーバとの接続
            this.name = name;
            server = new Socket(host, port);
            in = new BufferedReader(new InputStreamReader(
              server.getInputStream()));
            out = new PrintWriter(server.getOutputStream());

            // loginコマンドの送付
            out.println("login " + name);
            out.flush();
            repaint();
        }catch(Exception e){
            e.printStackTrace();
            System.exit(1);
        }
    }

    // logoutメソッド
    // logout処理を行います
    void logout(){
        try {
            // logoutコマンドの送付
            out.println("logout");
            out.flush();
            server.close();
        }catch (Exception e){
            ;
        }
        System.exit(0);
    }

    // repaintメソッド
    // サーバからゲームの情報を得て,クライアントの画面を描き直します
    void repaint(){
        // サーバにstatコマンドを送付し,盤面の様子などの情報を得ます
        out.println("stat");
        out.flush();

        try {
            String line = in.readLine();// サーバからの入力の読み込み
            Graphics g = c.getGraphics();// Canvas cに海の様子を描きます

            // 海の描画(単なる青い四角形です)
            g.setColor(Color.blue);
            g.fillRect(0, 0, 256, 256);

            //ship_infoから始まる船の情報の先頭行を探します
            while (!"ship_info".equalsIgnoreCase(line))
                line = in.readLine();

            // 船の情報ship_infoの表示
            // ship_infoはピリオドのみの行で終了です
            line = in.readLine();
            while (!".".equals(line)){
                boolean self = false;
                StringTokenizer st = new StringTokenizer(line);
                // 名前を読み取ります
                String obj_name = st.nextToken().trim();

                // 自分の船は赤(red)で表示し,他人の船は緑(green)で表示します
                if (obj_name.equals(name)){//自分の船
                    g.setColor(Color.red);
                    self = true;
                }
                else{ // 他人の船
                    g.setColor(Color.green);
                }

                // 船の位置座標を読み取ります
                int x = Integer.parseInt(st.nextToken()) ;
                int y = Integer.parseInt(st.nextToken()) ;

                //memorize ship pos
                if(self){
                    int round_x = Math.round((x+5)/10)*10;
                    int round_y = Math.round((y+5)/10)*10;
                    selfpos.setLocation(round_x,round_y);
                }

                double point = Double.parseDouble(st.nextToken());
                point = Math.round(point*10.0)/10.0;
                if(point < 0) point=0;

                // 船を表示します
                g.fillOval(x - 10, 256 - y - 10, 20, 20);
                // 得点を船の右下に表示します
                g.drawString(String.valueOf(point),x+10,256-y+10) ;
                // 名前を船の右上に表示します
                g.drawString(obj_name,x+10,256-y-10) ;

                // 次の１行を読み取ります
                line = in.readLine();
            }

            // energy_infoから始まる,燃料タンクの情報を待ち受けます
            while (!"energy_info".equalsIgnoreCase(line))
                line = in.readLine();

            // 燃料タンクの情報energy_infoの表示
            // energy_infoはピリオドのみの行で終了です
            line = in.readLine();
            while (!".".equals(line)){
                StringTokenizer st = new StringTokenizer(line);

                // 燃料タンクの位置座標を読み取ります
                int x = Integer.parseInt(st.nextToken()) ;
                int y = Integer.parseInt(st.nextToken()) ;
                
                int round_x = Math.round((x+5)/10)*10;
                int round_y = Math.round((y+5)/10)*10;
                fuelpos = new Point2D.Double(round_x,round_y);
                double dist = selfpos.distance(fuelpos);
                fuelList.put(dist, fuelpos);

                // 燃料タンクは,白抜きの赤丸で示します
                g.setColor(Color.red);
                g.fillOval(x - 5, 256 - y - 5, 10, 10);
                g.setColor(Color.white);
                g.fillOval(x - 3, 256 - y - 3, 6, 6);

                // 次の１行を読み取ります
                line = in.readLine();
            }
            if(!fuelList.isEmpty()){
                planPath();
                if(!path.isEmpty()){
                    sendCommand((String)path.remove(path.size()-1));
                }
                else{
                    System.out.println("path is empty");
                }
            }
            fuelList.clear();
        }catch (Exception e){
        e.printStackTrace();
        System.exit(1);
        }
    }

    public void planPath(){
        //pick closest fuel
        
        double min_dist = 9000;
        Enumeration e = fuelList.keys();
        while(e.hasMoreElements()){
            double element = (double)e.nextElement();
            if (element < min_dist){
                min_dist = element;
            }
        }
        destination = (Point2D.Double)fuelList.remove(min_dist);
        
        //breadth first search
        boolean found = false;
        boolean resign = false;
        int[][] closed_list = new int[300][300];
        int[][] action = new int[300][300];
        ArrayList open_list = new ArrayList();
        Point2D.Double node = new Point2D.Double();

        for(int i=0; i<300;i++){
            for(int j=0; j<300;j++){
                closed_list[i][j] = 0;
                action[i][j] = -1;
            }
        }
        open_list.add(selfpos);
        

        while((!found) && (!resign)){
            if(open_list.isEmpty()) resign = true;
            else{
                node = (Point2D.Double)open_list.remove(0);
                int x = (int)node.getX();
                int y = (int)node.getY();
                if ((x == (int)destination.getX()) && (y == (int)destination.getY())) found = true;
                else{
                    for(int i=0; i<delta.length; i++){
                        int x2 = x + delta[i][0];
                        int y2 = y + delta[i][1];
                        if((x2>=0)&&(x2<300)&&(y2>=0)&&(y2<300)){
                            if(closed_list[x2][y2] == 0){
                                open_list.add(new Point2D.Double(x2,y2));
                                closed_list[x2][y2] = 1;
                                action[x2][y2] = i;
                            }
                        }
                    }
                }
            }
        }
        if(found){
            int x = (int)destination.getX();
            int y = (int)destination.getY();
            int i = 0;
            while((x!=(int)selfpos.getX())||(y!=(int)selfpos.getY())){
                int x2 = x - delta[action[x][y]][0];
                int y2 = y - delta[action[x][y]][1];
                path.add(move[action[x][y]]);
                x = x2;
                y = y2;
                i++;
            }
        }
        else{
            System.out.println("no plan found");
        }
    }

    // sendCommandメソッド
    // サーバへコマンドを送信します
    public void sendCommand(String s){
        if ("up".equals(s)){
            out.println("up");
        }else if ("down".equals(s)){
            out.println("down");
        }else if ("left".equals(s)){
            out.println("left");
        }else if ("right".equals(s)){
            out.println("right");
        }
        out.flush();
    }

    // mainメソッド
    // UmiClientを起動します
    public static void main(String[] arg){
        new UmiAI();
    }
}
