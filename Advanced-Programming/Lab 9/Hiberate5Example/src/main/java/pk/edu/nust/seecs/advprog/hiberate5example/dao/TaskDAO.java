package pk.edu.nust.seecs.advprog.hiberate5example.dao;


import java.util.Iterator;
import java.util.List;


import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.service.ServiceRegistry;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Task;
import pk.edu.nust.seecs.advprog.hiberate5example.util.HibernateUtil;

public class TaskDAO {
	static ServiceRegistry  serviceRegistry ;
	static SessionFactory sessionFactory;
    static Session session;
	
	public TaskDAO(){
		// TODO Auto-generated method stub
        sessionFactory = HibernateUtil.getSessionFactory();
        session = sessionFactory.openSession();
        //nested Transactions are not supported. Once you have started transaction here
        // can't do that in the saveEmployee method.
        //session.beginTransaction();
	}
	
	public void saveEmployee(List<Task> newEmpList){
		Transaction t=session.beginTransaction();  
            for (Task newEmpList1 : newEmpList) {
                session.persist((Task) newEmpList1);
            }
      		t.commit(); 
	}

	public void printEmployees()
	{
		List<Task> emp = session.createQuery("from Task").list();
		Iterator<Task> it = emp.iterator();
		Task tempEmp;
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
