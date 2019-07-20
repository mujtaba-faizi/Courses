/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pk.edu.nust.seecs.advprog.hiberate5example.bo;

/**
 *
 * @author Fahad Satti <fahad.satti@seecs.edu.pk>
 */
public interface EmployeeBo {

    int addContractEmployee(int empIndex, float pay_per_hour, String contract_period);

    int addEmployee(String name);

    int addRegularEmployee(int empIndex, float salary, int bonus);

    void saveEmployees();
    
}
