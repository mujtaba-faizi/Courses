package pk.edu.nust.seecs.advprog.hiberate5example.dao;

import java.util.Iterator;
import java.util.List;


import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.service.ServiceRegistry;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Employee;
import pk.edu.nust.seecs.advprog.hiberate5example.util.HibernateUtil;

public class EmployeeDao {
	static ServiceRegistry  serviceRegistry ;
	static SessionFactory sessionFactory;
    static Session session;
	
	public EmployeeDao(){
		// TODO Auto-generated method stub
        sessionFactory = HibernateUtil.getSessionFactory();
        session = sessionFactory.openSession();
        //nested Transactions are not supported. Once you have started transaction here
        // can't do that in the saveEmployee method.
        //session.beginTransaction();
	}
	
	public void saveEmployee(List<Employee> newEmpList){
		Transaction t=session.beginTransaction();  
            for (Employee newEmpList1 : newEmpList) {
                session.persist((Employee) newEmpList1);
            }
      		t.commit(); 
	}

	public void printEmployees()
	{
		List<Employee> emp = session.createQuery("from Employee").list();
		Iterator<Employee> it = emp.iterator();
		Employee tempEmp;
		for(;it.hasNext(); )
		{
			tempEmp = it.next();
			System.out.println(tempEmp);
		}
	}
	
	public void closeSession()
	{
        session.close();
        sessionFactory.close();
	}
}
