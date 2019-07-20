/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pk.edu.nust.seecs.advprog.hiberate5example.view;

import pk.edu.nust.seecs.advprog.hiberate5example.bo.EmployeeBo;
import pk.edu.nust.seecs.advprog.hiberate5example.bo.impl.EmployeeBoImpl;

/**
 *
 * @author deser_000
 */
public class HibernateUnionSubClassTest {
    private EmployeeBo employeeHandler = new EmployeeBoImpl();
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        HibernateUnionSubClassTest hbt = new HibernateUnionSubClassTest();
        hbt.doAll();
    }
    
    /**
     * Perform all action here
     */
    public void doAll(){
        int emp1Id = employeeHandler.addEmployee("fahad");
        int emp2Id = employeeHandler.addEmployee("Obaid");
        int emp3Id = employeeHandler.addEmployee("Zohaib");
        int emp4Id = employeeHandler.addEmployee("Sadaf");
        
        employeeHandler.addRegularEmployee(emp1Id, 1.0f , 0);
        employeeHandler.addContractEmployee(emp2Id, 0.3f , "1 year");
        employeeHandler.addContractEmployee(emp3Id, 0.2f , "1 year");
        employeeHandler.addContractEmployee(emp4Id, 0.6f , "2 years");
        
        
        employeeHandler.saveEmployees();
    }
}
