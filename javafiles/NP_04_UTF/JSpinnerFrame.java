import javax.swing.JFrame;
import javax.swing.JSpinner;
import javax.swing.SpinnerNumberModel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.BorderLayout;

public class JSpinnerFrame extends JFrame
                           implements ActionListener {
  private SpinnerNumberModel model;

  public JSpinnerFrame() {
    super("スピナー");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    model = new SpinnerNumberModel(0, -100, 100, 1);
    JSpinner spinner = new JSpinner(model);
    getContentPane().add(spinner, BorderLayout.CENTER);
    JButton button = new JButton("実行");
    button.addActionListener(this);
    getContentPane().add(button, BorderLayout.EAST);
    pack();
  }

  public void actionPerformed(ActionEvent event) {
    int value = model.getNumber().intValue();
    System.out.println("値は" + value);
  }

  public static void main(String[] args) {
    JSpinnerFrame frame = new JSpinnerFrame();
    frame.setVisible(true);
  }
}
