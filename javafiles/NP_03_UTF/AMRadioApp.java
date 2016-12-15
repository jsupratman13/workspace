import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.ImageIcon;
import java.awt.Container;
import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Color;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class AMRadioApp extends JFrame implements ActionListener{
  private JButton b1,b2,b3,b4,b5,b6;
  private JLabel label,label2;
  private JCheckBox checkBox;
  private ImageIcon icon1,icon2;
  private int iconFlag = 0;

  public AMRadioApp() {
    super("AMRadioApp");
    setDefaultCloseOperation(EXIT_ON_CLOSE);
    Container container = getContentPane();

	//top layer
	JPanel panelTop = new JPanel();
	container.add(panelTop, BorderLayout.NORTH);
	//mid layer
    JPanel panelMid = new JPanel();
    //panelMid.setLayout(new BorderLayout());
    container.add(panelMid, BorderLayout.CENTER);
	FlowLayout layout = new FlowLayout();
	panelMid.setLayout(layout);
	//bottom layer
	JPanel panelBottom = new JPanel();
	panelBottom.setLayout(new BorderLayout());
	container.add(panelBottom, BorderLayout.SOUTH);
	//bottom left layer, bottom right layer
	JPanel panelBL = new JPanel();
	panelBL.setLayout(new BorderLayout());
	panelBottom.add(panelBL, BorderLayout.WEST);
	JPanel panelBR = new JPanel();
	panelBR.setLayout(new BorderLayout());
	panelBottom.add(panelBR, BorderLayout.CENTER);

	//text
    label = new JLabel("Press button for music");
    panelTop.add(label, BorderLayout.CENTER);

	//set 6 button
    b1 = new JButton("Music1");
	b1.addActionListener(this);
    panelMid.add(b1);
	b2 = new JButton("Music2");
    panelMid.add(b2);
	b2.addActionListener(this);
	b3 = new JButton("Music3");
	panelMid.add(b3);
	b3.addActionListener(this);
	b4 = new JButton("Music4");
	panelMid.add(b4);
	b4.addActionListener(this);
	b5 = new JButton("Music5");
	panelMid.add(b5);
	b5.addActionListener(this);
	b6 = new JButton("Music6");
	panelMid.add(b6);
	b6.addActionListener(this);

	//checkbox
	checkBox = new JCheckBox("display image");
	checkBox.addActionListener(this);
	panelBL.add(checkBox, BorderLayout.SOUTH);
	//images
	icon1 = new ImageIcon("R0010176.jpg");
	icon2 = new ImageIcon("kirby.png");
	label2 = new JLabel(icon1);
	panelBR.add(label2, BorderLayout.CENTER);


	pack();
  }

  public void actionPerformed(ActionEvent event){
		if(event.getSource() == b1){
			label.setText("Listening to Music 1");
		}
		else if(event.getSource() == b2){
			label.setText("Listening to Music 2");
		}
		else if(event.getSource() == b3){
			label.setText("Listening to Music 3");
		}
		else if(event.getSource() == b4){
			label.setText("Listening to Music 4");
		}
		else if(event.getSource() == b5){
			label.setText("Listening to Music 5");
		}
		else if(event.getSource() == b6){
			label.setText("Listening to Music 6");
		}

		if(checkBox.isSelected()){
			label2.setIcon(icon2);
		} else{
			label2.setIcon(icon1);
		}
  }

  public static void main(String[] args) {
    AMRadioApp frame = new AMRadioApp();
    frame.setVisible(true);
  }
}
