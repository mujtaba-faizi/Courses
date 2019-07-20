

object Strassen_Algo {
  def main(args:Array[String]){
     
    val matrixA=Array.ofDim[Int](2,2)   //declaring matrices with fixed values
    val matrixB=Array.ofDim[Int](2,2)
    matrixA(0)(0)=2
    matrixA(0)(1)=4
    matrixA(1)(0)=1
    matrixA(1)(1)=5
    matrixB(0)(0)=3
    matrixB(0)(1)=6
    matrixB(1)(0)=7
    matrixB(1)(1)=9
   
        println("Matrix A:")   //example of 2*2 matrix
    show(matrixA)  
        println("Matrix B:")
    show(matrixB)
     println("Result:")
    show(mult(matrixA,matrixB))
   

    
     println("Enter the size of matrix e.g. 4 represents 4*4 matrix(but only in power of 2: ")
    val size=scala.io.StdIn.readInt()
           val matrixC=Array.ofDim[Int](size,size) 
     for (i <- 0 to size-1) {
         for ( j <- 0 to size-1) {
           val a=scala.util.Random
            matrixC(i)(j)=a.nextInt()  //random integers
         }
      }
    Breakdown(2,2,matrixC,size)
  }
  def Breakdown(u:Int,v:Int,X:Array[Array[Int]],size:Int){
                    if(size==1){
                     return //multiply all list elements i.e. all arrays
                    }

      val A=Array.ofDim[Int](2,2)   
    val B=Array.ofDim[Int](2,2)
 
            for (i <- u-2 to u-1) {
         for ( j <- v-2 to v-1) {
            A(i)(j)=X(i)(j)
            if(j+2>=u)    //adding elements acc. to the index values of the big matrix
            B(i)(j)=X(i)(j-2)  
            else
            B(i)(j)=X(i)(j+2)
         }
      }
        println("Matrix split:")
        show(A)
        println("Matrix split:")
        show(B)    
  
         //add arrays in list to multiply in the end; multiply inside the recursion break condition
 Breakdown(u+2,v+2,X,size/2)   //using recursion  
    
  }
  def show(X:Array[Array[Int]]){

          for (i <- 0 to 1) {
         for ( j <- 0 to 1) {
           print(X(i)(j))
           print("  ")
           if (i==0 && j==1){
             println("")
           }
         }
      }
           println("")
  }
 def P1(X:Array[Array[Int]],Y:Array[Array[Int]]):Int={
      
   return X(0)(0)*(Y(0)(1)-Y(1)(1))
 }
 def P2(X:Array[Array[Int]],Y:Array[Array[Int]]):Int={
   return Y(1)(1)*(X(0)(0)+X(0)(1))
 }
 def P3(X:Array[Array[Int]],Y:Array[Array[Int]]):Int={
   return Y(0)(0)*(X(1)(0)+X(1)(1))
 }
  def P4(X:Array[Array[Int]],Y:Array[Array[Int]]):Int={
   return X(1)(1)*(Y(1)(0)-Y(0)(0))
 }
   def P5(X:Array[Array[Int]],Y:Array[Array[Int]]):Int={
   return (X(1)(1)+X(0)(0))*(Y(0)(0)+Y(1)(1))
 }
    def P6(X:Array[Array[Int]],Y:Array[Array[Int]]):Int={
   return (X(0)(1)-X(1)(1))*(Y(1)(0)+Y(1)(1))
 }
     def P7(X:Array[Array[Int]],Y:Array[Array[Int]]):Int={
   return (X(0)(0)-X(1)(0))*(Y(0)(0)+Y(0)(1))
 }
      def mult(X:Array[Array[Int]],Y:Array[Array[Int]]):Array[Array[Int]]={
         val result=Array.ofDim[Int](2,2)
         result(0)(0)=P6(X,Y)+P5(X,Y)+P4(X,Y)-P2(X,Y)
         result(0)(1)=P1(X,Y)+P2(X,Y)
         result(1)(0)=P3(X,Y)+P4(X,Y)
         result(1)(1)=P1(X,Y)+P5(X,Y)-P3(X,Y)-P7(X,Y)
   return result
 }
}