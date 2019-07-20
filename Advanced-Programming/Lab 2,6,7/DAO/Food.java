package DAO;
import 	Lab2.*;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

import com.mysql.jdbc.CallableStatement;
import com.mysql.jdbc.PreparedStatement;
public class Food {
	  
	    private String Name;
	    private int FoodID;
	    private int Price;
	    private int Amount;
	    private int time_to_make;
	    
	    public int getId() {
	        return FoodID;
	    }
	    public void setId(int id) {
	        this.FoodID = id;
	    }
	    public String getName() {
	        return Name;
	    }
	    public void setName(String name) {
	        this.Name = Name;
	    }
	    public static boolean search(Statement s,String a) throws SQLException {
	    	ResultSet rs = s.executeQuery("SELECT * FROM food");
	    	while (rs.next()){    
			    String value1 = rs.getString(1);   
	    	 System.out.println(value1);}
	    	ResultSet r = s.executeQuery("SELECT * FROM food");
			while (r.next()){    
				    String value1 = r.getString(1);   
				   
	   if(a.equals(value1)) 
		   return true;
	    }
			return false;
	    }
public static void main(String[] args) throws ClassNotFoundException, SQLException{
	Scanner sc=new Scanner(System.in);
	PreparedStatement prep=null;
				Ecafe_JDBC a=new Ecafe_JDBC();
				Connection con=a.getCon();
				Statement statement = con.createStatement();
				System.out.println("Enter a food item to search in the restaurant");
				String item=sc.next();
				boolean b=search(statement,item);
				if (b==true)
					System.out.println(item+" exists");
				else
					System.out.println(item+" doesnt exist");

				//insert query   
				String sql = "Insert into Food(Name,FoodID,Price,Amount,Time_to_make) values(?,?,?,?,?)";   
				prep = (PreparedStatement) con.prepareStatement(sql); 
				//Bind values into the parameters.             
				prep.setString(1, "Faizi");              
				prep.setInt(2, 984);
				prep.setInt(3, 45);
				prep.setInt(4, 2);
				prep.setInt(5, 55);
				int rows = prep.executeUpdate(); 
				
				//search query1
				PreparedStatement prep_s=null;
				 sql = "SELECT Name FROM Food WHERE Price=?";             
				  prep_s = (PreparedStatement) con.prepareStatement(sql); 
				//Bind values into the parameters. 
				  prep_s.setInt(1,45);
					ResultSet result = prep_s.executeQuery(); 
					System.out.println("Items with price 45rs: ");
					while (result.next()){    
						System.out.println(result.getString("Name")); } 
					
					//callable statement
					CallableStatement cstmt = null; 
					String SQL = "{call getFoodName (?, ?)}";   
					cstmt = (CallableStatement) con.prepareCall (SQL);    
					// set int IN parameter 
					cstmt.setInt(1, 7); // register int OUT parameter 
					cstmt.registerOutParameter(2, java.sql.Types.VARCHAR); 
					cstmt.execute();
					// get String OUTOUT 
					String OUT = cstmt.getString(2);
					System.out.println("Food item with ID : 7=="+OUT);

				}


}
