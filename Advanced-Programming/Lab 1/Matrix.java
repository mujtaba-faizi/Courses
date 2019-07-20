import java.util.Scanner;

public class Matrix {


	private double[][] array;
	private int rows;
	private int cols;
	private String name;  //user specified name for his/her matrix
	
	Matrix(String e,int r, int s){
		name=e;
		rows=r;
		cols=s;
	}
	String getName() {
		return name;
	}
	
public void show(double[][] array) {   //displays the array in matrix format
	System.out.println("Matrix:-");
	for(int i=0;i<rows;i++) {
		for(int j=0;j<cols;j++) {
			if ((i==1 && j==0)||(i==2 && j==0)||(i==3 && j==0)||(i==4 && j==0)) {   //to display the next row elements in next line
				System.out.println("");
				System.out.print(array[i][j]+"  ");
			}
			else{
				System.out.print(array[i][j]+"  ");
			}
		}
	}
System.out.println("");
}

public double[][] add(double[][] a,double[][] b,int e,int f,int g,int h) {
	double[][] c=new double[e][f];
	if (e==g && f==h) {
	for (int i=0;i<e;i++) {
		for(int j=0;j<f;j++) {
			c[i][j]= a[i][j]+b[i][j];
		}
	}
	return c;}
	else {
		System.out.println("Size should be same of both matrices");
		return null;
	}
}
public double[][] subt(double[][] a,double[][] b,int e,int f,int g,int h) {
	double[][] c=new double[e][f];
	if (e==g && f==h) {
	for (int i=0;i<e;i++) {
		for(int j=0;j<f;j++) {
			c[i][j]= a[i][j]-b[i][j];
		}
	}
	return c;}
	else {
		System.out.println("Size should be same of both matrices");
		return null;
	}
}

public double[][] scalarMult(double[][] a,double b,int e,int f) {
	double[][] c=new double[e][f]; 
	for (int i=0;i<e;i++) {
		for(int j=0;j<f;j++) {
			c[i][j]= a[i][j]*b;
		}
	}
	return c;
}

public boolean equal(double[][] a,double[][] b,int r,int c) {
	for (int i=0;i<r;i++) {
		for(int j=0;j<c;j++) {
			if(a[i][j]!= b[i][j]) {
				return false;
			}
		}
	}
	return true;
}

public double[][] mult(double[][] a,double[][] b,int e,int f,int g,int h) {
	double[][] c=new double[e][h];
	if (e==f) {
		 for (int i = 0; i < e; i++)
	            for (int j = 0; j < h; j++)
	                for (int k = 0; k < f; k++)
	                    c[i][j] += (a[i][k] * b[k][j]);
	return c;}
	else {
		System.out.println("Size not correct for multiplication");
		return null;
	}	
}

public double[][] transpose(double[][] a,int g,int h) {
	double[][] c=new double[h][g];
	for (int i = 0; i < g; i++)
        for (int j = 0; j < h; j++)
            c[j][i] = a[i][j];    //interchanging the cols with rows for taking transpose
    return c;
}

public double[][] inverse(double a[][]) 
{
    int n = a.length;
    double x[][] = new double[n][n];
    double b[][] = new double[n][n];
    int index[] = new int[n];
    for (int i=0; i<n; ++i) 
        b[i][i] = 1;
    
    gaussian(a, index);    // Transform the matrix into an upper triangle

    for (int i=0; i<n-1; ++i)   // Update the matrix b[i][j] with the ratios stored
        for (int j=i+1; j<n; ++j)
            for (int k=0; k<n; ++k)
                b[index[j]][k]
                	    -= a[index[j]][i]*b[index[i]][k];

    for (int i=0; i<n; ++i) // Perform backward substitutions
    {
        x[n-1][i] = b[index[n-1]][i]/a[index[n-1]][n-1];
        for (int j=n-2; j>=0; --j) 
        {
            x[j][i] = b[index[j]][i];
            for (int k=j+1; k<n; ++k) 
            {
                x[j][i] -= a[index[j]][k]*x[k][i];
            }
            x[j][i] /= a[index[j]][j];
        }
    }
    return x;
}

//Method to carry out the partial-pivoting Gaussian elimination.  Here index[] stores pivoting order.

public static void gaussian(double a[][], int index[]) 
{
    int n = index.length;
    double c[] = new double[n];

    for (int i=0; i<n; ++i) // Initialize the index
        index[i] = i;

    for (int i=0; i<n; ++i) // Find the rescaling factors, one from each row
    {
        double c1 = 0;
        for (int j=0; j<n; ++j) 
        {
            double c0 = Math.abs(a[i][j]);
            if (c0 > c1) c1 = c0;
        }
        c[i] = c1;
    }

    int k = 0;   // Search the pivoting element from each column
    for (int j=0; j<n-1; ++j) 
    {
        double pi1 = 0;
        for (int i=j; i<n; ++i) 
        {
            double pi0 = Math.abs(a[index[i]][j]);
            pi0 /= c[index[i]];
            if (pi0 > pi1) 
            {
                pi1 = pi0;
                k = i;
            }
        }

        int itmp = index[j];  // Interchange rows according to the pivoting order
        index[j] = index[k];
        index[k] = itmp;
        for (int i=j+1; i<n; ++i) 	
        {
            double pj = a[index[i]][j]/a[index[j]][j];

            a[index[i]][j] = pj;   // Record pivoting ratios below the diagonal

            for (int l=j+1; l<n; ++l)   // Modify other elements accordingly
                a[index[i]][l] -= pj*a[index[j]][l];
        }
    }
}


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
        System.out.println("Enter a name for your matrix");
        String m1=scan.next();
        
        System.out.println("Enter the rows and columns for your 2-D matrix");
 		int rows1=scan.nextInt();
 		int cols1=scan.nextInt();
 		double[][] arr1=new double[rows1][cols1];
		System.out.println("Enter the values for a 2-D matrix");
		for (int i=0;i<rows1;i++) {
			for(int j=0;j<cols1;j++) {
				int element = scan.nextInt();
				arr1[i][j]=element;
			}
		}
		Matrix Matrix1=new Matrix(m1,rows1,cols1);
		Matrix1.show(arr1);
		
		System.out.println("Enter a name for your second matrix");
		String m2=scan.next();
		System.out.println("Enter the rows and columns for your 2-D matrix");
 		int rows2=scan.nextInt();
 		int cols2=scan.nextInt();
 		double[][] arr2=new double[rows2][cols2];
		System.out.println("Enter the values for a 2-D matrix");
		for (int i=0;i<rows2;i++) {
			for(int j=0;j<cols2;j++) {
				int element = scan.nextInt();
				arr2[i][j]=element;
			}
		}
		Matrix Matrix2=new Matrix(m2,rows2,cols2);
		Matrix2.show(arr2);
			
		System.out.println("Now enter a valid equation on the matrices you specified");
		String eq = scan.next();   //can't use same matrix again for another operation
		        eq=eq+" ";                                   //have to add a space at the end to avoid error:string index out of index
		
		
		
		
		//using ^ for inverse and ! for transpose and x for scalar multiplication
        //in order of precedence   
        	if (eq.contains(m1)==true)     //charAt() specifies a particular character in a string
        	{
        		if (eq.charAt(eq.indexOf(m1)+1)=='!') {     //if ! is after the matrix name
        			StringBuilder sb = new StringBuilder(eq);
        			sb.deleteCharAt((eq.indexOf(m1)+1));
        			eq=sb.toString();
        			arr1=Matrix1.transpose(arr1, rows1, cols1);   //updating the same matrix
        			Matrix1.show(arr1);
        		}
if (eq.charAt(eq.indexOf(m1)+1)=='^') {     //if ^ is after the matrix name
        			
        			arr1=Matrix1.inverse(arr1);
        			StringBuilder sb = new StringBuilder(eq);
        			sb.deleteCharAt((eq.indexOf(m1)+1));
        			eq=sb.toString();
        			Matrix1.show(arr1);
        		}
if(eq.charAt(eq.indexOf(m1)+1)=='x') {
	double myd= Double.parseDouble(Character.toString(eq.charAt(eq.indexOf(m1)+2)));
	arr1=Matrix1.scalarMult(arr1, myd, rows1, cols1);
	StringBuilder sb = new StringBuilder(eq);
	sb.deleteCharAt((eq.indexOf(m1)+1));
	sb.deleteCharAt((eq.indexOf(m1)+1));
	eq=sb.toString();
	Matrix1.show(arr1);
        	}
if(eq.charAt(eq.indexOf(m1)+1)=='+') {
	arr1=Matrix1.add(arr1,arr2, rows1, cols1,rows2,cols2);
	if(arr1!=null) {
		Matrix1.show(arr1);} 
        	}
if(eq.charAt(eq.indexOf(m1)+1)=='-') {
	arr1=Matrix1.subt(arr1,arr2, rows1, cols1,rows2,cols2);
	if(arr1!=null) {
		Matrix1.show(arr1);} 
        	}
if(eq.charAt(eq.indexOf(m1)+1)=='*') {
	arr1=Matrix1.mult(arr1,arr2, rows1, cols1,rows2,cols2);   
	Matrix1.show(arr1);
        	}
        	}
        	
        	
        	
        	 if(eq.contains(m2)==true )
        	{
if (eq.charAt(eq.indexOf(m2)+1)=='!') {     //if ! is after the matrix name
	StringBuilder sb = new StringBuilder(eq);
	sb.deleteCharAt((eq.indexOf(m2)+1));
	eq=sb.toString();
        			arr2=Matrix2.transpose(arr2, rows1, cols1);
        			Matrix2.show(arr2);
        		}
if (eq.charAt(eq.indexOf(m2)+1)=='^') {     //if ^ is after the matrix name
	StringBuilder sb = new StringBuilder(eq);
	sb.deleteCharAt((eq.indexOf(m2)+1));
	eq=sb.toString();
	arr2=Matrix2.inverse(arr2);
	Matrix2.show(arr2);
}
if(eq.charAt(eq.indexOf(m2)+1)=='x') {
	double myd= Double.parseDouble(Character.toString(eq.charAt(eq.indexOf(m2)+2)));
	arr2=Matrix2.scalarMult(arr2, myd, rows2, cols2);
	StringBuilder sb = new StringBuilder(eq);
	sb.deleteCharAt((eq.indexOf(m2)+1));
	sb.deleteCharAt((eq.indexOf(m2)+1));
	eq=sb.toString();
	Matrix2.show(arr2);
        	}
if(eq.charAt(eq.indexOf(m2)+1)=='+') {
	arr2=Matrix2.add(arr1,arr2, rows1, cols1,rows2,cols2);
	if(arr2!=null) {
		Matrix2.show(arr2);} 
        	}
if(eq.charAt(eq.indexOf(m2)+1)=='-') {
	arr2=Matrix2.subt(arr1,arr2, rows1, cols1,rows2,cols2);
	if(arr2!=null) {
		Matrix2.show(arr2);} 
        	}
        	}
        	 if(eq.charAt(eq.indexOf(m2)+1)=='*') {
        			arr2=Matrix2.mult(arr2,arr1, rows1, cols1,rows2,cols2);   
        			Matrix2.show(arr2);
        		        	}
		
		
	}

}