

object lab{
  var len=10
    def main(args: Array[String]) {
//task1
  val list = List(3,2,1,4,5,676,2,0,33,232)
  println("Enter no. to find nth Last Element: ")
  val nth=scala.io.StdIn.readInt()
  println("nth Last Element of the List: "+ println(find(nth,list)))
  println(isPrime(2,4))//task3   
        if(Coprimes(5,7))  //task4
      println("The numbers given are coprimes")
    else
      println("The numbers are not coprimes")
  println(_xor(true,true))//task5
  println(_and(true,false))//task6
  println(_nand(false,false))//task7

    }
     def greatestcommondivisor(a: Int, b: Int): Int = {
    if (b == 0)
      a
    else
      greatestcommondivisor(b, a % b)
  }
  def Coprimes(m: Int, n: Int): Boolean ={
    greatestcommondivisor(m, n) == 1
  }



    //task3
def isPrime(a:Int,b:Int) :Boolean={

if (b==a){
  return true
}
if(b%a==0){
  return false
}
  isPrime(a+1,b)

}

//task4

def find( nth:Int, list:List[Int] ):Int  = {
  val value = len-nth
  return list(value);
  
}




def _xor(a:Boolean,b:Boolean):Boolean={   //task5
  if(a==b)
    false
  else
    true
}

def _nand(a:Boolean,b:Boolean):Boolean={   //task7
   return _not(_and(a,b))   //uses the "not" and "and" functions
}  

  
  def _not(a:Boolean):Boolean={
    
    if(a == true)
    return false
    else
      return true
  }
  
  def _and(a:Boolean,b:Boolean):Boolean={  //task6
    
    if(a == true && b==true)
    return true
    else
      return false
  
}
  


  }

