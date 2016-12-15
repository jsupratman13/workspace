import javax.swing.JFrame;
import javax.swing.Box;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.Container;
import java.awt.BorderLayout;
import java.awt.Component;

public class BoxFrame2 extends JFrame {
  public BoxFrame2() {
    super("ボックス");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    Container container = getContentPane();
    Box box = Box.createVerticalBox();
    container.add(box, BorderLayout.WEST);

    JButton button1 = new JButton("1つ目のボタン");
    box.add(button1);
    Component glue = Box.createGlue();
    box.add(glue);
    JButton button2 = new JButton("2つ目のボタン");
    box.add(button2);
    JButton button3 = new JButton("3つ目のボタン");
    box.add(button3);
    pack();
  }

  public static void main(String[] args) {
    BoxFrame2 frame = new BoxFrame2();
    frame.setVisible(true);
  }
}
