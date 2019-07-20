import static org.junit.Assert.*;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

public class matrix_test {

	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
	}

	@AfterClass
	public static void tearDownAfterClass() throws Exception {
	}

	@Test
	public void ADD() {
Matrix A=new Matrix("A",2,2);
		System.out.println("Addition method test:ADD()");
double[][] a= {{1,2,3},{1,2,3}};
double[][] b= {{4,5,6},{4,5,6}};
double[][] c=A.add(a, b, 2, 3, 2, 3);
double[][] d= {{5,7,9},{5,7,9}};

		 assertTrue(A.equal(c, d, 2, 3));
	 
	}
	@Test
	public void SUB() {
Matrix A=new Matrix("A",2,2);
		System.out.println("Subtraction method test:SUB()");
double[][] a= {{1,2,3},{1,2,3}};
double[][] b= {{4,5,6},{4,5,6}};
double[][] c=A.subt(b, a, 2, 3, 2, 3);
double[][] d= {{3,3,3},{3,3,3}};

		 assertTrue(A.equal(c, d, 2, 3));
	 
	}
	@Test
	public void Trans() {
Matrix A=new Matrix("A",2,2);
		System.out.println("Transpose method test:Trans()");
double[][] a= {{1,2},{4,5}};
double[][] c=A.transpose(a, 2, 2);
double[][] d= {{1,2},{4,5}};

		 assertTrue(A.equal(c, d, 2, 2));
	 
	}
	@Test
	public void Scalar() {
Matrix A=new Matrix("A",2,2);
		System.out.println("Scalar method test:Scalar()");
double[][] a= {{1,2,3},{4,5,6}};
double[][] c=A.scalarMult(a, 3, 2, 3);
double[][] d= {{3,6,9},{12,15,18}};

		 assertTrue(A.equal(c, d, 2, 3));
	 
	}
	@Test
	public void MULT() {
Matrix A=new Matrix("A",2,2);
		System.out.println("Multiplication method test:MULT()");
double[][] a= {{1,2},{3,4}};
double[][] b= {{1,2},{3,4}};
double[][] c=A.mult(a, b, 2, 2, 2, 2);
double[][] d= {{7,10},{15,22}};

		 assertTrue(A.equal(c, d, 2, 2));
	 
	}
}

