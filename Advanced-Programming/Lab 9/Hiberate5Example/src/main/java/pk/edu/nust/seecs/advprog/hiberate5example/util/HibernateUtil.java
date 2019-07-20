package pk.edu.nust.seecs.advprog.hiberate5example.util;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Contract_Employee;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Employee;
import pk.edu.nust.seecs.advprog.hiberate5example.model.Regular_Employee;


public class HibernateUtil {

	// A SessionFactory is set up once for an application!
        private static SessionFactory sessionFactory=null;

private static SessionFactory buildSessionFactory() {

    try {
        Configuration cfg = new Configuration();
        cfg.addAnnotatedClass(Employee.class);
        cfg.addAnnotatedClass(Contract_Employee.class);
        cfg.addAnnotatedClass(Regular_Employee.class);
        cfg.configure();
        sessionFactory = cfg.buildSessionFactory();
        return sessionFactory;
        
    }
    catch (Exception e) {
        // The registry would be destroyed by the SessionFactory, but we had trouble building the SessionFactory
        // so destroy it manually.
        
        throw new ExceptionInInitializerError(e);
    }
}

public static SessionFactory getSessionFactory() {
    if(sessionFactory==null){
        buildSessionFactory();
    }
    return sessionFactory;
}
}