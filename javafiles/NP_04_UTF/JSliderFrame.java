import javax.swing.JFrame;
import javax.swing.JSlider;
import javax.swing.JLabel;
import java.awt.Container;
import java.awt.BorderLayout;
import javax.swing.event.ChangeListener;
import javax.swing.event.ChangeEvent;

public class JSliderFrame extends JFrame
                          implements ChangeListener {
  JSlider slider = null;
  JLabel label = null;

  public JSliderFrame() {
    super("スライダー");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    Container container = getContentPane();
    slider = new JSlider(JSlider.HORIZONTAL,-100,100,0);
    slider.setMajorTickSpacing(50);
    slider.setMinorTickSpacing(10);
    slider.setPaintTicks(true);
    slider.setPaintLabels(true);
    container.add(slider, BorderLayout.CENTER);
    label = new JLabel("0");
    container.add(label, BorderLayout.EAST);
    pack();

    slider.addChangeListener(this);
  }

  public void stateChanged(ChangeEvent event) {
    int value = slider.getValue();
    label.setText(new Integer(value).toString());
  }

  public static void main(String[] args) {
    JSliderFrame frame = new JSliderFrame();
    frame.setVisible(true);
  }
}
