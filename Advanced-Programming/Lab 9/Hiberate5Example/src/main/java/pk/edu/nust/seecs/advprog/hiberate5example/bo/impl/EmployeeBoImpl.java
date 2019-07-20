/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pk.edu.nust.seecs.advprog.hiberate5example.bo.impl;

import java.util.ArrayList;
import java.util.List;
import pk.edu.nust.seecs.advprog.hiberate5example.bo.EmployeeBo;
import pk.edu.nust.seecs.advprog.hiberate5example.dao.EmployeeDao;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Contract_Employee;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Employee;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Regular_Employee;

/**
 *
 * @author Fahad Satti <fahad.satti@seecs.edu.pk>
 */
public class EmployeeBoImpl implements EmployeeBo {

    public List<Employee> employeeRoster;

    public EmployeeBoImpl() {
        employeeRoster = new ArrayList<>();
    }

    @Override
    public int addEmployee(String name) {
        Employee tempEmp = new Employee();
        tempEmp.setName("name");

        employeeRoster.add(tempEmp);
        return employeeRoster.indexOf(tempEmp);
    }

    @Override
    public int addRegularEmployee(int empIndex, float salary, int bonus) {

        Regular_Employee tempRegEmp = new Regular_Employee();
        tempRegEmp.setSalary(salary);
        tempRegEmp.setBonus(bonus);
        employeeRoster.add(empIndex,tempRegEmp);
        return employeeRoster.indexOf(tempRegEmp);
    }

    @Override
    public int addContractEmployee(int empIndex, float pay_per_hour, String contract_period) {

        Contract_Employee tempConEmp = new Contract_Employee();
        tempConEmp.setContract_period(contract_period);
        tempConEmp.setPay_per_hour(pay_per_hour);
        employeeRoster.add(empIndex,tempConEmp);
        return employeeRoster.indexOf(tempConEmp);
    }

    @Override
    public void saveEmployees() {
        EmployeeDao empD = new EmployeeDao();
        empD.saveEmployee(employeeRoster);
    }
}
