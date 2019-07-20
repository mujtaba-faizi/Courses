package clock;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.JButton;

public class thread {
	private String time;
	thread(String a){
		time=a;
	}
	public int run(){
        int x=0;
        DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
                System.out.println("An alarm is in execution");
          while(x==0) {
        	  
        	  Date date = new Date();
        	  if(time==(dateFormat.format(date))) {
        		  System.out.print("Alarm is going off");
        		  break;
        	  }
          }
		return 1;
    }

	public void snooze() {
		time=time+5;
	}
	
	
}
