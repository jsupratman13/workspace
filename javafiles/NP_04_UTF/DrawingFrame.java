import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.Container;
import java.awt.BorderLayout;
import java.awt.Graphics;
import java.awt.Dimension;

class DrawingPanel extends JPanel {
  public void paint(Graphics g) {
    Dimension dim = getSize();
    g.setColor(getBackground());
    g.fillRect(0, 0, dim.width, dim.height);
    g.setColor(getForeground());
    g.drawOval(0, 0, dim.width - 1, dim.height - 1);
  }

  public Dimension getPreferredSize() {
    return (new Dimension(200, 200));
  }
}

public class DrawingFrame extends JFrame {
  public DrawingFrame() {
    super("楕円");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    Container container = getContentPane();
    container.add(new DrawingPanel(),
                  BorderLayout.CENTER);
    pack();
  }

  public static void main(String[] args) {
    DrawingFrame frame = new DrawingFrame();
    frame.setVisible(true);
  }
}
