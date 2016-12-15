import javax.swing.JFrame;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import java.awt.Container;
import java.awt.BorderLayout;

public class JComboBoxFrame extends JFrame {
  public JComboBoxFrame() {
    super("コンボボックス");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    Container container = getContentPane();
    DefaultComboBoxModel model = new DefaultComboBoxModel();
    model.addElement("1番目");
    model.addElement("2番目");
    model.addElement("3番目");
    model.addElement("4番目");
    model.addElement("5番目");
    model.addElement("6番目");
    model.addElement("7番目");
    model.addElement("8番目");
    model.addElement("9番目");
    JComboBox comboBox = new JComboBox(model);
    container.add(comboBox, BorderLayout.CENTER);
	comboBox.setEditable(true);
    pack();
  }

  public static void main(String[] args) {
    JComboBoxFrame frame = new JComboBoxFrame();
    frame.setVisible(true);
  }
}
