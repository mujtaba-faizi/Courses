package Lab2;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Ecafe_JDBC {
	Connection connection;
public Ecafe_JDBC() throws ClassNotFoundException, SQLException {
	String url="";
	String username="root";
	String password="";
	Class.forName("com.mysql.jdbc.Driver");
	connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/ecafe", username,password); 
}
public Connection getCon() {
	return connection;
}
}

