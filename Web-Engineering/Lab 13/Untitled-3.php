<?php


class a{
      public $userid;
	  public $fname;
	  public $lname;
	  public $dob;
	  
	  public function show(){
		  echo $this->userid. " ".$this->fname." ".$this->lname." ".$this->dob."<br>";
	  }
}

$conn=mysqli_connect('localhost','root','');

	 
	 $query="select * from form";    
	 $result=mysqli_query($conn,$query);
	 $obj=array();
	 
	 if ($query)
	 {
			 $x=0;
			 while ($row = mysqli_fetch_object($result,'a'))
			 {
				 $obj[$x]=$row;
				 $x++;	 
			 }
		 
		 foreach($obj as $temp)
		 {
			 echo $temp->user_id;
			 echo "&nbsp; &nbsp; &nbsp; ";
			 echo $temp->fname;
			 echo " ";
			 echo $temp->lname;
			 echo "&nbsp; &nbsp; &nbsp; ";	
			 echo $temp->dob;
			 echo "<br>";	 
		 }
		 
	 }	 
	
?>