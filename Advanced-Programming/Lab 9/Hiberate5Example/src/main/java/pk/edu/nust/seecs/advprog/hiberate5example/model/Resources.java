package pk.edu.nust.seecs.advprog.hiberate5example.model;

import java.util.ArrayList;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
@Entity
public class Resources {
	@ManyToMany
	ArrayList<Employee> emp=new ArrayList<Employee>();
	@Id
	private int res_id;
	/**
	 * @return the res_id
	 */
	public int getRes_id() {
		return res_id;
	}
	/**
	 * @param res_id the res_id to set
	 */
	public void setRes_id(int res_id) {
		this.res_id = res_id;
	}
}
