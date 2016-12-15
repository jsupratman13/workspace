import	javax.swing.JFrame;
import	javax.swing.JMenuBar;
import	javax.swing.JMenu;
import	javax.swing.JMenuItem;

public class MenuFrame2 extends JFrame {
	public MenuFrame2() {
		super("menu");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		
		JMenu fileMenu = new JMenu("file");
		menuBar.add(fileMenu);
		JMenu newMenu = new JMenu("new");
		fileMenu.add(newMenu);
		JMenuItem gifMenu = new JMenuItem("GIF");
		newMenu.add(gifMenu);
		JMenuItem jpegMenu = new JMenuItem("JPEG");
		newMenu.add(jpegMenu);
		JMenuItem openMenu = new JMenuItem("open");
		fileMenu.add(openMenu);
		JMenuItem saveMenu = new JMenuItem("save");
		fileMenu.add(saveMenu);
		fileMenu.addSeparator();
		JMenuItem optionMenu = new JMenuItem("option");
		fileMenu.add(optionMenu);
		
		setSize(200,200);
	}
	
	public static void main(String[] args) {
		MenuFrame2 frame = new MenuFrame2();
		frame.setVisible(true);
	}
}
