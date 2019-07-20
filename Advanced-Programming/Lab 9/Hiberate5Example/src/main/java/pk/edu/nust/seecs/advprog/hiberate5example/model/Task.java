package pk.edu.nust.seecs.advprog.hiberate5example.model;

import java.util.ArrayList;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Entity  
@Table(name = "con_tasks") 
@AttributeOverrides({
    @AttributeOverride(name="name", column=@Column(name="name")),
    @AttributeOverride(name="status", column=@Column(name="status"))
})
public class Task implements OperationService{
	@OneToOne
	Contract_Employee contract_emp=new Contract_Employee();
	@OneToMany
	ArrayList <Regular_Employee> reg_emp=new ArrayList <Regular_Employee>();
	@Id
	private int task_id;
	private String name;
	private String status;
	@Override
	public String startTask() {

		return "Start Task";
	}
	@Override
	public String endTask() {
		
		return "End Task";
	}
	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}
	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}
	/**
	 * @return the status
	 */
	public String getStatus() {
		return status;
	}
	/**
	 * @param status the status to set
	 */
	public void setStatus(String status) {
		this.status = status;
	}
	
}
