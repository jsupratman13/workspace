import	javax.swing.JFrame;
import	javax.swing.JMenuBar;
import	javax.swing.JMenu;
import	javax.swing.JMenuItem;

public class MenuFrame extends JFrame {
	public MenuFrame() {
		super("image");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		JMenu fileMenu = new JMenu("file");
		menuBar.add(fileMenu);
		JMenuItem openMenu = new JMenuItem("open");
		fileMenu.add(openMenu);
		setSize(200,200);
	}
	
	public static void main(String[] args) {
		MenuFrame frame = new MenuFrame();
		frame.setVisible(true);
	}
}
