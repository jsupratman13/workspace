import javax.swing.JFrame;
import javax.swing.JList;
import javax.swing.DefaultListModel;
import javax.swing.JScrollPane;
import java.awt.Container;
import java.awt.BorderLayout;

public class JListFrame extends JFrame {
  public JListFrame() {
    super("リスト");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    Container container = getContentPane();
    DefaultListModel model = new DefaultListModel();
    model.addElement("1番目");
    model.addElement("2番目");
    model.addElement("3番目");
    model.addElement("4番目");
    model.addElement("5番目");
    model.addElement("6番目");
    model.addElement("7番目");
    model.addElement("8番目");
    model.addElement("9番目");
    JList list = new JList(model);
    container.add(new JScrollPane(list), BorderLayout.CENTER);
    pack();
  }

  public static void main(String[] args) {
    JListFrame frame = new JListFrame();
    frame.setVisible(true);
  }
}
