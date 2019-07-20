<html>
<head>
	<title>2</title>
</head>
<body>

<?php
 $servername = "localhost";
$username = "root";
$password = "";
$dbname = "a";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

	 $userid = $_POST['userid'];
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


$conn->close();
?>



</body>
</html>