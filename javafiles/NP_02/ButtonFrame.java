import	javax.swing.JFrame;
import	javax.swing.JLabel;
import	javax.swing.JButton;
import	java.awt.BorderLayout;
import	java.awt.Container;

public class ButtonFrame extends JFrame {
	public ButtonFrame() {
		super("button frame");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		JLabel label = new JLabel("This is a label");
		Container container = getContentPane();
		container.add(label, BorderLayout.CENTER);
		JButton button = new JButton("button");
		container.add(button, BorderLayout.SOUTH);
		pack();
	}
	
	public static void main(String[] args) {
		ButtonFrame frame = new  ButtonFrame();
		frame.setVisible(true);
	}
}
