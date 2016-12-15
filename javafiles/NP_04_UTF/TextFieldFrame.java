import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.BorderLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class TextFieldFrame extends JFrame
                            implements ActionListener {
  private JTextField textField;

  public TextFieldFrame() {
    super("テキストフィールド");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    textField = new JTextField("サンプル", 10);
    getContentPane().add(textField, BorderLayout.CENTER);
    JButton button = new JButton("タイトル変更");
    button.addActionListener(this);
    getContentPane().add(button, BorderLayout.EAST);
    pack();
  }

  public void actionPerformed(ActionEvent event) {
    String text = textField.getText();
    setTitle(text);
  }

  public static void main(String[] args) {
    TextFieldFrame frame = new TextFieldFrame();
    frame.setVisible(true);
  }
}
