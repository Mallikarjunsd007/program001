public class DevOpsEngineer extends Employee { 
    private double bonus; 
    public DevOpsEngineer(String name, int employeeId, double salary, double bonus) { 
    super(name, employeeId, salary); 
    this.bonus = bonus; 
    } 
    public void displayDetails() {
        super.displayDetails(); 
System.out.println("Bonus: Rs." + bonus); 
System.out.println("Total Salary: Rs." + (salary + bonus)); 
} 
public static void main(String[] args) { 
DevOpsEngineer engineer = new DevOpsEngineer("Sourabh", 101, 50000, 10000); 
engineer.displayDetails(); 
} 
}
    

