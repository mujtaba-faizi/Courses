/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pk.edu.nust.seecs.springlogaspects.bo;

import java.util.ArrayList;
import javax.swing.JTextArea;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author a_bas
 */
public class StudentBoImplTest {
    
    public StudentBoImplTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
    }
    
    @After
    public void tearDown() {
    }

    /**
     * Test of sayHello method, of class StudentBoImpl.
     */
    @Test
    public void testSayHello() {
        System.out.println("sayHello");
        Integer studentId = null;
        StudentBoImpl instance = new StudentBoImpl();
        instance.sayHello(studentId);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of getInfo method, of class StudentBoImpl.
     */
    @Test
    public void testGetInfo() {
        System.out.println("getInfo");
        StudentBoImpl instance = new StudentBoImpl();
        String expResult = "";
        String result = instance.getInfo();
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of printCourses method, of class StudentBoImpl.
     */
    @Test
    public void testPrintCourses() {
        System.out.println("printCourses");
        JTextArea outputText = null;
        StudentBoImpl instance = new StudentBoImpl();
        instance.printCourses(outputText);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of addStudents method, of class StudentBoImpl.
     */
    @Test
    public void testAddStudents() {
        System.out.println("addStudents");
        String studentName = "";
        ArrayList<Integer> studentCourses = null;
        StudentBoImpl instance = new StudentBoImpl();
        Integer expResult = null;
        Integer result = instance.addStudents(studentName, studentCourses);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }
    
}
