package pk.edu.nust.seecs.advprog.hiberate5example.model;

import java.util.ArrayList;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.OneToMany;
import javax.persistence.Table;

@Entity
@Table(name = "reg_emp_unionsubclass")
@AttributeOverrides({
    @AttributeOverride(name = "empID", column = @Column(name = "id")),
    @AttributeOverride(name = "empName", column = @Column(name = "name")),})
public class Regular_Employee extends Employee {
	@OneToMany
	ArrayList<Task> tasks=new ArrayList<Task>();
    int bonus;
    float salary;

    @Override
    public String toString() {
        return "Regular_Employee{" + "bonus=" + bonus + ", salary=" + salary + '}';
    }

    public int getBonus() {
        return bonus;
    }

    public void setBonus(int bonus) {
        this.bonus = bonus;
    }

    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }
}
