import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.ImageIcon;
import java.awt.Graphics;
import java.awt.Dimension;
import java.awt.Container;
import java.awt.BorderLayout;

class DrawingPanel extends JPanel {
  public void paint(Graphics g) {
    Dimension dim = getSize();
    g.setColor(getBackground());
    g.fillRect(0, 0, dim.width, dim.height);
    ImageIcon icon = new ImageIcon("4dd.jpg");
    g.drawImage(icon.getImage(), 0, 0, this);
  }

  public Dimension getPreferredSize() {
    return (new Dimension(200, 200));
  }
}

public class ImageFrame extends JFrame {
  public ImageFrame() {
    super("描画");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    Container container = getContentPane();
    container.add(new DrawingPanel(),
                  BorderLayout.CENTER);
    pack();
  }

  public static void main(String[] args) {
    ImageFrame frame = new ImageFrame();
    frame.setVisible(true);
  }
}
