import  javax.swing.JFrame;
import  javax.swing.JLabel;
import  java.awt.Container;
import  java.awt.BorderLayout;
import	javax.swing.ImageIcon;


public class LabelFrame extends JFrame {
    public LabelFrame() {
        super("java network programming");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
       // JLabel label = new JLabel("Network Programming on java");
        JLabel label = new JLabel(new ImageIcon("R0010176.jpg"));
        Container container = getContentPane();
        container.add(label, BorderLayout.CENTER);
        pack();
    }
    
    public static void main(String[] args) {
        LabelFrame frame = new LabelFrame();
        frame.setVisible(true);
    }
}
