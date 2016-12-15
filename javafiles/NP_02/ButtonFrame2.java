import	javax.swing.JFrame;
import	javax.swing.JLabel;
import	javax.swing.JButton;
import	java.awt.BorderLayout;
import	java.awt.Container;
import	java.awt.event.ActionListener;
import	java.awt.event.ActionEvent;

public class ButtonFrame2 extends JFrame implements ActionListener {
	private JLabel label = null;
	
	public ButtonFrame2() {
		super("button frame");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		label = new JLabel("This is a label");
		Container container = getContentPane();
		container.add(label, BorderLayout.CENTER);
		JButton button = new JButton("button");
		button.addActionListener(this);
		container.add(button, BorderLayout.SOUTH);
		pack();
	}
	
	public void actionPerformed(ActionEvent event) {
		label.setText("button pushed!!!");
	}
	
	public static void main(String[] args) {
		ButtonFrame2 frame = new  ButtonFrame2();
		frame.setVisible(true);
	}
}
