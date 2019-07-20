<?php


$N=$_POST["name"];
$dob=$_POST["DOB"];
$gender=$_POST["gender"];

$getdate=strtotime($dob);
//echo "<br>";
$var=date("Y",$getdate);

$age=2017-$var;

echo $age;
echo "<br>";

 
if($gender=="male" && $age>40) {
	echo "you are eligbile for PM";
}elseif ($gender=="female" && $age>30) {
	echo "you are eligbile for PM";
}else{
	echo "you are not eligbile for PM";
}


?>