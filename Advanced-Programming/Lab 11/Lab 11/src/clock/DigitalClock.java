package clock;

import java.awt.EventQueue;
import java.util.TimeZone;
import java.util.concurrent.TimeUnit;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.BorderLayout;
import javax.swing.JRadioButton;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.CardLayout;
import java.awt.GridLayout;

public class DigitalClock {

	private JFrame frame;

	/**
	 * Launch the application.
	 */
	private static String displayTimeZone(TimeZone tz) {

		long hours = TimeUnit.MILLISECONDS.toHours(tz.getRawOffset());
		long minutes = TimeUnit.MILLISECONDS.toMinutes(tz.getRawOffset())
                                  - TimeUnit.HOURS.toMinutes(hours);
		// avoid -4:-30 issue
		minutes = Math.abs(minutes);

		String result = "";
		if (hours > 0) {
			result = String.format("(GMT+%d:%02d) %s", hours, minutes, tz.getID());
		} else {
			result = String.format("(GMT%d:%02d) %s", hours, minutes, tz.getID());
		}

		return result;

	}
	
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					DigitalClock window = new DigitalClock();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public DigitalClock() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(new GridLayout(1, 0, 0, 0));
		
	    JLabel l1;  
	    l1=new JLabel("Select timezone");  
	    l1.setBounds(50,100, 900,30);   
	    frame.add(l1);
	    frame.setSize(300,300);  
	    frame.setLayout(null);  
	    frame.setVisible(true);  	    

		String[] country = TimeZone.getAvailableIDs();     
		
	    JComboBox cb=new JComboBox(country);    
	    cb.setBounds(50, 50,90,20);    
	    frame.add(cb);       
	    
	    JButton b=new JButton("Show timezone");  
	    b.setBounds(50,150, 90,30); 
	    frame.add(b);
	    b.setSize(200, 30);
	    
		String[] ids = TimeZone.getAvailableIDs();
		  b.addActionListener(new ActionListener() {  
		        public void actionPerformed(ActionEvent e) {
		l1.setText(displayTimeZone(TimeZone.getTimeZone((String) cb.getItemAt(cb.getSelectedIndex()))));
		        }  
		  });  
		  
		    JButton button=new JButton("Add alarms");  
		    button.setBounds(50,200, 90,30); 
		    frame.add(button);
      	    button.setSize(200, 30);
		    
			  button.addActionListener(new ActionListener() {  
			        public void actionPerformed(ActionEvent e) {
			        Alarms();
			        }  
			  }); 

	}

	
	void Alarms() {
		
		JFrame frame2 = new JFrame();
		frame2.setBounds(100, 100, 450, 300);
		frame2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame2.getContentPane().setLayout(new GridLayout(1, 0, 0, 0));
		frame2.setVisible(true);
		
		JButton button2=new JButton("Add alarm");  
	    button2.setBounds(50,50, 50,30); 
	    frame2.add(button2);
  	    button2.setSize(50, 30);
  	    
		  button2.addActionListener(new ActionListener() {  
		        public void actionPerformed(ActionEvent e) {
		        thread alarm=new thread("2017:12:12 12:12:12");
		        int c=alarm.run();

  				JButton button3=new JButton("Snooze");  
		        if(c==0) {
				    button3.setBounds(50,50, 50,30); 
				    frame2.add(button3);
			  	    button3.setSize(50, 30);
		        }
				  button3.addActionListener(new ActionListener() {  
				        public void actionPerformed(ActionEvent e) {
				        alarm.snooze();
				        alarm.run();
				        }  
				  }); 
		        }  
		  }); 
	}

}
