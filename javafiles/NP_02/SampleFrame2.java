import javax.swing.JFrame;

public class SampleFrame2 extends JFrame {
	public SampleFrame2() {
		super("Network Programming!");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setSize(200,200);
	}
	
	public static void main(String[] args) {
		SampleFrame2 frame = new SampleFrame2();
		frame.setVisible(true);
	}
}
