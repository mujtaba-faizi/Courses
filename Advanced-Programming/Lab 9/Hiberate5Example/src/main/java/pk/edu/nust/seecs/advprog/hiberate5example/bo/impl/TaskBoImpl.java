package pk.edu.nust.seecs.advprog.hiberate5example.bo.impl;

import java.util.ArrayList;
import java.util.List;

import pk.edu.nust.seecs.advprog.hiberate5example.bo.TaskBo;
import pk.edu.nust.seecs.advprog.hiberate5example.dao.EmployeeDao;
import pk.edu.nust.seecs.advprog.hiberate5example.dao.TaskDAO;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Employee;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Task;

public class TaskBoImpl implements TaskBo{
    public List<Task> employeeRoster;

    public TaskBoImpl() {
        employeeRoster = new ArrayList<>();
    }
	
	
	@Override
	public int addTask(int a, String b, String c) {
        Task tempEmp = new Task();
        tempEmp.setName(b);
        tempEmp.setStatus(c);
        
        employeeRoster.add(tempEmp);
        return employeeRoster.indexOf(tempEmp);
	}

	@Override
	public void saveTask() {
		// TODO Auto-generated method stub
        TaskDAO empD = new TaskDAO();
        empD.saveEmployee(employeeRoster);
	}

}
