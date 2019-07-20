package pk.edu.nust.seecs.advprog.hiberate5example.model;


import javax.persistence.*;

@Entity  
@Table(name = "con_emp_unionsubclass")  
@AttributeOverrides({
	@AttributeOverride(name="empID", column=@Column(name="id")),
	@AttributeOverride(name="empName", column=@Column(name="name")),
})

public class Contract_Employee extends Employee{
	@OneToOne
	Task tasks=new Task();
	float pay_per_hour;
	String contract_period;
	
	public float getPay_per_hour() {
		return pay_per_hour;
	}
	public void setPay_per_hour(float pay_per_hour) {
		this.pay_per_hour = pay_per_hour;
	}
	public String getContract_period() {
		return contract_period;
	}
	public void setContract_period(String contract_period) {
		this.contract_period = contract_period;
	}
	
	
}
