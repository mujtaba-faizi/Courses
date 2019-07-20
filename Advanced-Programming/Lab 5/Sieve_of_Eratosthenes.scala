
import org.junit.Test
import org.junit.Assert._


object Sieve_of_Eratosthenes {
  def getList(a:List[Int],b:Int,c:Int):List[Int]={
    if(b>c){
      return a
    }
      val d=List(b)   
    getList(a++d,b+1,c)  //a++d merges the two lists
  }
  
  def remMultiple(a:Int,c:List[Int],b:Int):List[Int]={      //removes multiples
    if(a>b)   //if a reaches greater than the squareroot of n, then exit recursion
      return c
     remMultiple(a+1,c.filterNot((p)=>(p%a==0 && a!=p)),b)   //filters out the elements whose multiples doesnt exist in the list(i.e. whose mod with the values a is 0) and the itself is not removed
  }
  @Test
  def list_test(){      //test for n=15 and getList() func
        val correct=List(2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    val a=List()
    val list=getList(a,2,15)
    assertEquals(correct,list)
    println("test successful")   //otherwise raise exception
  }
  @Test
  def prime_test(){     //test for n=15 and remMultiple() func
    val correct=List(2,3,5,7,11,13)
    val a=List()
    val list=getList(a,2,15)
    assertEquals(correct,remMultiple(2,list,15^(1/2)))
    println("test successful")   //otherwise raise exception
  }
 def main(args:Array[String]){
   println("Enter the value of n: ")
    val n = scala.io.StdIn.readInt()
    val a=List()
    val list=getList(a,2,n)
   list.foreach(println)
   println("Prime:-")
   val sq=scala.math.sqrt(n).toInt
   val prime= remMultiple(2,list,n^(1/2))
   prime.foreach(println)
   
   list_test()     //unit test for correct list
   prime_test()    //unit test for correct prime numbers
  
 }
}