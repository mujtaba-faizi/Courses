package Lab2;

import java.util.Calendar;
import java.util.Scanner;

public class Cafe {

private int Order;
private int quantity;
private int App;
private int Soup;
private int SideDish;
private int MainDish;
private int pickup;
private String address;


	Cafe(){
     
	}
	int getBill(int a,int b) {
		
    	if (a==1 || a==2 ||a==3 ||a==4) 
    		return b*200;    
    	
    	else if(a==5 || a==6)
    		return b*300;
    	
    	else if(a==7 || a==8 || a==9 || a==10 ||a==11 ||a==12)
    		return b*1500;
    	
    	else if(a==13 || a==14 || a==15)
    		return b*700;
    	
    	return 0;
	}
    void ShowMenu() {
    	 System.out.println("-----------");
    	 System.out.println("MENU");
    	 System.out.println("-----------");
    	 System.out.println("Appetizers:-");
    	 System.out.println("1.mozerella 2.pineapple disk 3.cucumber salad 4.French toast");
    	 System.out.println("Soups:-");
    	 System.out.println("5.Carrot 6.Cucumber");
    	 System.out.println("Main course dishes:-");
    	 System.out.println("7.Roast 8.Chicken Palao 9.Channa Daal 10.Pizza 11.Chicken Burger 12.Fried Rice");
    	 System.out.println("Side course dishes:-");
    	 System.out.println("13.Choclate 14.Chips 15.Curly Fries");
    }
    public int getTime(int a, int b) {  //time for cooks to make a dish
    	
    	if (a==1 || a==2 ||a==3 ||a==4) 
    		return (b*5)/4;    //   dividing by 4 since 4 chefs are available
    	
    	else if(a==5 || a==6)
    		return (b*7)/4;
    	
    	else if(a==7 || a==8 || a==9 || a==10 ||a==11 ||a==12)
    		return (b*15)/4;
    	
    	else if(a==13 || a==14 || a==15)
    		return (b*10)/4;
    	
    	return 0;
    }



	public static void main(String[] args) {
		int deliveryTime=0;
		  Scanner scan = new Scanner(System.in);
		Calendar calendar = Calendar.getInstance();
for (int j=0;j<1000;j++) {
	System.out.println("New order? press 0 for yes and 1 for no");
	int u=scan.nextInt();
	if(u==1)break;
	  Cafe Gloria=new Cafe();

	  Gloria.ShowMenu();  //shows the dishes
	  int time=0;    //increments for each dish
	  int bill=0;
	  for (int i=0;i<1000;i++) {
		  System.out.println("Enter a number to order a specific dish and press 0 to stop ordering");
		  int order=scan.nextInt();
		  if(order==0)break;
		  System.out.print("Enter quantity of that dish");
		  int quan=scan.nextInt();
		
		  time=time+Gloria.getTime(order,quan);
		bill=bill+Gloria.getBill(order, quan);
				  
	  }
	  time=time+deliveryTime;
	  int hours = calendar.get(Calendar.HOUR_OF_DAY);
		int t = calendar.get(Calendar.MINUTE)+(hours*60);  //current time in minutes
		
		if((t+time)>1320 || (t+time)<660)    
			System.out.print("Sorry, your order will surpass closing time or too early for cafe to open");
		else {
		System.out.println("Your order will take "+time+" minutes");
		System.out.println("Bill: "+bill+" Rs");
		
			deliveryTime=deliveryTime+time;
		
		}}
 		
	}

}