package Lab2;

import static org.junit.Assert.*;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

public class CafeTest {

	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
	}

	@AfterClass
	public static void tearDownAfterClass() throws Exception {
	}

	@Test
	public void BILL() {
Cafe A=new Cafe();
		

assertEquals(  200, A.getBill(1,1));
assertEquals(600,A.getBill(5, 2));
assertEquals(3000,A.getBill(8, 2));
	 
	}
	@Test
	public void TIME() {
		Cafe A=new Cafe();
		assertEquals(  1, A.getTime(1, 1));
		assertEquals(11,A.getBill(13, 3));
	}

}
