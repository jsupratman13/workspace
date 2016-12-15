import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.Container;
import java.awt.BorderLayout;

public class ContainerFrame2 extends JFrame {
  public ContainerFrame2() {
    super("パネル");
    setDefaultCloseOperation(EXIT_ON_CLOSE);
    Container container = getContentPane();
    JLabel label = new JLabel("いずれかのボタンを押してください");
    container.add(label, BorderLayout.CENTER);
    JPanel panel = new JPanel();
    panel.setLayout(new BorderLayout());
    container.add(panel, BorderLayout.SOUTH);
    JButton button1 = new JButton("左のボタン");
    panel.add(button1, BorderLayout.NORTH);
    JButton button2 = new JButton("右のボタン");
    panel.add(button2, BorderLayout.EAST);
    pack();
  }

  public static void main(String[] args) {
    ContainerFrame2 frame = new ContainerFrame2();
    frame.setVisible(true);
  }
}
