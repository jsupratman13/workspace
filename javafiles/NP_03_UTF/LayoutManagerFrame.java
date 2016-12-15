import	javax.swing.JFrame;
import	javax.swing.JButton;
import	java.awt.Container;
import	java.awt.BorderLayout;
import	java.awt.Color;

public class LayoutManagerFrame extends JFrame {
	public LayoutManagerFrame() {
		super("BorderLayout");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		Container container = getContentPane();
		JButton north = new JButton("north");
		north.setBackground(Color.blue);
		container.add(north, BorderLayout.NORTH);
		JButton west = new JButton("west");
		west.setBackground(Color.yellow);
		container.add(west, BorderLayout.WEST);
		JButton center = new JButton("center");
		center.setBackground(Color.gray);
		container.add(center, BorderLayout.CENTER);
		JButton east = new JButton("east");
		east.setBackground(Color.red);
		container.add(east, BorderLayout.EAST);
		JButton south = new JButton("south");
		south.setBackground(Color.green);
		container.add(south, BorderLayout.SOUTH);
		pack();
	}
		
	public static void main(String[] args) {
		LayoutManagerFrame frame = new LayoutManagerFrame();
		frame.setVisible(true);
	}
}
		
