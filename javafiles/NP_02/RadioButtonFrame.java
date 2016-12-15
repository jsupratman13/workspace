import	javax.swing.JFrame;
import	javax.swing.JLabel;
import	javax.swing.JRadioButton;
import	javax.swing.ButtonGroup;
import	java.awt.BorderLayout;
import	java.awt.Container;
import	java.awt.event.ActionListener;
import	java.awt.event.ActionEvent;

public class RadioButtonFrame extends JFrame implements ActionListener {
	private JLabel label = null;
	private JRadioButton radioButton1 = null;
	private JRadioButton radioButton2 = null;
	
	public RadioButtonFrame() {
		super("Radio button");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		label = new JLabel("Which do you want?");
		Container container = getContentPane();
		container.add(label, BorderLayout.NORTH);
		ButtonGroup group = new ButtonGroup();
		radioButton1 = new JRadioButton("Professional Baseball");
		group.add(radioButton1);
		radioButton1.addActionListener(this);
		container.add(radioButton1, BorderLayout.WEST);
		radioButton2 = new JRadioButton("JLeague");
		group.add(radioButton2);
		radioButton2.addActionListener(this);
		container.add(radioButton2, BorderLayout.EAST);
		pack();
	}
	
	public void actionPerformed(ActionEvent event) {
		if (radioButton1.isSelected()) {
			label.setText("Pro Baseball is the best!");
		} else {
			label.setText("JLeague of course!");
		}
	}
		
	public static void main(String[] args) {
		RadioButtonFrame frame = new RadioButtonFrame();
		frame.setVisible(true);
	}
}
