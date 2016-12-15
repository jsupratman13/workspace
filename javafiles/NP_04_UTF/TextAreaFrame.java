import javax.swing.JFrame;
import javax.swing.JTextArea;
import javax.swing.JScrollPane;
import javax.swing.JButton;
import java.awt.BorderLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class TextAreaFrame extends JFrame
                           implements ActionListener {
  private JTextArea textArea;

  public TextAreaFrame() {
    super("テキストエリア");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    textArea = new JTextArea("サンプル", 5, 20);
    JScrollPane scrollPane = new JScrollPane(textArea);
    getContentPane().add(scrollPane, BorderLayout.CENTER);
    JButton button = new JButton("追加");
    button.addActionListener(this);
    getContentPane().add(button, BorderLayout.SOUTH);
    pack();
  }

  public void actionPerformed(ActionEvent event) {
    String text = textArea.getText();
    textArea.append("\n" + text);
  }

  public static void main(String[] args) {
    TextAreaFrame frame = new TextAreaFrame();
    frame.setVisible(true);
  }
}
