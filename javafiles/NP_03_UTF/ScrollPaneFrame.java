import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JLabel;
import javax.swing.ImageIcon;
import java.awt.Container;
import java.awt.BorderLayout;

public class ScrollPaneFrame extends JFrame {
  public ScrollPaneFrame() {
    super("ScrollPane");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    Container container = getContentPane();
    JLabel label = new JLabel(new ImageIcon("R0010176.jp"));
    JScrollPane scrollPane = new JScrollPane(label);
    container.add(srcollPane, BorderLayout.CENTER);
    pack();
  }

  public static void main(String[] args) {
    ScrollPaneFrame frame = new ScrollPaneFrame();
    frame.setVisible(true);
  }
}
