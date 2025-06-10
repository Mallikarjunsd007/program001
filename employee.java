public class Employee { 
    protected String name; 
    protected int employeeId; 
    protected double salary; 
    public Employee(String name, int employeeId, double salary) { 
    this.name = name; 
    this.employeeId = employeeId; 
    this.salary = salary; 
    } 
    public void displayDetails() { 
    System.out.println("Employee Name: " + name); 
    System.out.println("Employee ID: " + employeeId); 
    System.out.println("Salary: Rs." + salary); 
    } 
    }