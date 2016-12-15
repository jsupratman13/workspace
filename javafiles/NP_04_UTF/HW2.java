import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JSpinner;
import javax.swing.Box;
import javax.swing.SpinnerNumberModel;
import javax.swing.JTextField;
import javax.swing.ImageIcon;
import java.awt.Container;
import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Graphics;
import java.awt.Dimension;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.event.ChangeListener;
import javax.swing.event.ChangeEvent;
import java.math.*;

class DrawingPanel extends JPanel{
  public int width,height;
  public boolean trollmode;
  private ImageIcon icon;

  public DrawingPanel(){
	width = 20;
	height = 20;
	trollmode = false;
	icon = new ImageIcon("Trollface.jpg");
  }

  public void paint(Graphics g) {
    super.paintComponent(g);
	Dimension dim = getSize();
    g.setColor(getBackground());
    //g.fillRect(dim.width/4, dim.height/4, width, height);
    g.setColor(getForeground());
    g.drawOval(dim.width/2-width, dim.height/2-height, width*2-1, height*2-1);
	if (trollmode){
	   g.drawImage(icon.getImage(),0,0,this);
	}
  }

  public Dimension getPreferredSize() {
    return (new Dimension(350, 350));
  }
}

public class HW2 extends JFrame implements ChangeListener,ActionListener{
  private SpinnerNumberModel x,y;
  private JButton execute_button;
  private JTextField text;
  private DrawingPanel draw;
  private JPanel panelBottom;
  private boolean click;

  public HW2() {
    super("ellipse viewer");
    setDefaultCloseOperation(EXIT_ON_CLOSE);

    Container container = getContentPane();
		
	//oval images
	panelBottom = new JPanel();
	container.add(panelBottom, BorderLayout.CENTER);
	draw = new DrawingPanel();
    panelBottom.add(draw,BorderLayout.CENTER);

	//user interface
	JPanel panelTop = new JPanel();
	container.add(panelTop, BorderLayout.NORTH);
	FlowLayout layout1 = new FlowLayout();
	panelTop.setLayout(layout1);
	JPanel xPanel = new JPanel();
	JPanel yPanel = new JPanel();
	JPanel aPanel = new JPanel();
	panelTop.add(xPanel);
	panelTop.add(yPanel);
	panelTop.add(aPanel);

	JLabel label_x = new JLabel("x");
	xPanel.add(label_x);
	x = new SpinnerNumberModel(draw.width,1,273,1);
	JSpinner spinner_x = new JSpinner(x);
	xPanel.add(spinner_x);
	x.addChangeListener(this);

	JLabel label_y = new JLabel("y");
	yPanel.add(label_y);
	y = new SpinnerNumberModel(draw.height,1,286,1);
	JSpinner spinner_y = new JSpinner(y);
	yPanel.add(spinner_y);
	y.addChangeListener(this);

	JLabel label_a = new JLabel("area");
	aPanel.add(label_a);
	text = new JTextField(String.valueOf(Math.round(Math.PI*draw.width*draw.height*100.0)/100.0),7);
	aPanel.add(text);

	execute_button = new JButton("execute");
	panelTop.add(execute_button,BorderLayout.SOUTH);
	execute_button.addActionListener(this);
    
	click = false;
	pack();
  }

  public void stateChanged(ChangeEvent event){
    if(event.getSource() != execute_button){
  	  int x_value = x.getNumber().intValue();
	  int y_value = y.getNumber().intValue();
	  draw.width = x_value;
	  draw.height = y_value;
	  draw.repaint();
	  double area;
	  area = x_value*y_value*Math.PI;
	  text.setText(String.valueOf(Math.round(area*100.0)/100.0));
	}
  }

  public void actionPerformed(ActionEvent event){
    if(event.getSource() == execute_button){
		if(click){
			draw.trollmode = false;
			click = false;
		}else{
		    draw.trollmode = true;
			click = true;
	    }
		draw.repaint();
	}
  }
  public static void main(String[] args) {
    HW2 frame = new HW2();
	frame.setSize(400,400);
    frame.setVisible(true);
  }
}
