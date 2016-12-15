import	javax.swing.JFrame;
import	javax.swing.JLabel;
import	javax.swing.JCheckBox;
import	javax.swing.ImageIcon;
import	java.awt.BorderLayout;
import	java.awt.event.ActionListener;
import	java.awt.event.ActionEvent;

public class CheckBoxFrame extends JFrame implements ActionListener {
	private JLabel label = null;
	private JCheckBox checkBox = null;
	private JCheckBox checkBox2 = null;
	private ImageIcon icon1 = null;
	private ImageIcon icon2 = null;
	private ImageIcon icon3 = null;
	
	public CheckBoxFrame() {
		super("Check Box");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		icon1 = new ImageIcon("R0010211.jpg");
		icon2 = new ImageIcon("R0010212.jpg");
		icon3 = new ImageIcon("kirby.png");
		label = new JLabel(icon1);
		getContentPane().add(label, BorderLayout.CENTER);
		checkBox = new JCheckBox("Eat?");
		checkBox.addActionListener(this);
		getContentPane().add(checkBox, BorderLayout.SOUTH);
		checkBox2 = new JCheckBox("Summon Demon!");
		checkBox2.addActionListener(this);
		getContentPane().add(checkBox2, BorderLayout.EAST);
		pack();
	}
	
	public void actionPerformed(ActionEvent event) {
		if (checkBox2.isSelected()){
			label.setIcon(icon3);
		}
		else if (checkBox.isSelected()) {
			label.setIcon(icon2);
		} else {
			label.setIcon(icon1);
		}
	}
	
	public static void main(String[] args) {
		CheckBoxFrame frame = new CheckBoxFrame();
		frame.setVisible(true);
	}
}
