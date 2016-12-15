import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.Color;

public class FlowLayoutFrame extends JFrame {
  public FlowLayoutFrame() {
    super("BorderLayout");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    Container container = getContentPane();
    FlowLayout layout = new FlowLayout();
    container.setLayout(layout);

    JButton north = new JButton("north");
    north.setBackground(Color.blue);
    container.add(north);
    JButton west = new JButton("west");
    west.setBackground(Color.yellow);
    container.add(west);
    JButton center = new JButton("center");
    center.setBackground(Color.gray);
    container.add(center);
    JButton east = new JButton("east");
    east.setBackground(Color.red);
    container.add(east);
    JButton south = new JButton("south");
    south.setBackground(Color.green);
    container.add(south);
    pack();
  }

  public static void main(String[] args) {
    FlowLayoutFrame frame = new FlowLayoutFrame();
    frame.setVisible(true);
  }
}
