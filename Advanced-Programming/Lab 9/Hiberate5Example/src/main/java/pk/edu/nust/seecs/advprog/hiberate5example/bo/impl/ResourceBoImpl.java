package pk.edu.nust.seecs.advprog.hiberate5example.bo.impl;

import java.util.ArrayList;
import java.util.List;

import pk.edu.nust.seecs.advprog.hiberate5example.bo.ResourcesBo;
import pk.edu.nust.seecs.advprog.hiberate5example.dao.EmployeeDao;
import pk.edu.nust.seecs.advprog.hiberate5example.dao.ResourcesDAO;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Resources;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Task;;

public class ResourceBoImpl implements ResourcesBo{
    public List<Resources> employeeRoster;

    public ResourceBoImpl() {
        employeeRoster = new ArrayList<>();
    }
	@Override
	public int addTask(int a) {
		 Resources tempEmp = new Resources();
	        tempEmp.setRes_id(a);
	        
	        employeeRoster.add(tempEmp);
	        return employeeRoster.indexOf(tempEmp);
	}

	@Override
	public void saveResource() {
        ResourcesDAO empD = new ResourcesDAO();
        empD.saveResources(employeeRoster);
		
	}

}
