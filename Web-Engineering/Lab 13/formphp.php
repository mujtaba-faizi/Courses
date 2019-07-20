<?php 

     $conn=mysqli_connect('localhost','root','');
	 
	 if(!$conn)
	 {
       echo 'Not connected to Server';	 
	 }
	 
	 if(!mysqli_select_db($conn,'database'))
	 {
	   echo 'Database not Selected !' ;
	 }
	 
	 $userid = $_POST['user_id'];
	 $fname = $_POST['fname'];
	 $lname = $_POST['lname'];
	 $dob = $_POST['dob'];
	 
	 if (mysqli_query($conn,"CALL procedure('".$userid."','".$fname."','".$lname."','".$dob."')"))
	 {
	   echo 'Inserted';
	 }
	 else
	 {
	   echo 'Not Inserted, Username already exists !';
	 }

?> 