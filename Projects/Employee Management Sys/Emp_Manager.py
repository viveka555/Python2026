from Employee import Employee

class EmployeeManager:

    def __init__(self):
        self.employees = []

# Method for adding employees
    def add_employee(self, name, age, salary):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                print("Employee already exist!")
                return
        
        new_employee = Employee(name,age,salary)
        self.employees.append(new_employee)
        print("Employee added successfully...")

#Method for listing employee

    def list_employee(self):
        if not self.employees:
            print("Employee not found!!!")

        print("\n----Employee list----")
        for emp in self.employees:
            print(emp)
        print()
#Method for Deleting employees within a specified age range.

    def delete_emp_by_age_range(self, min_age,max_age):
        original_count = len(self.employees)
        self.employees = [emp for emp in self.employees if not(min_age <= emp.age <=max_age)]
        deleted_emp = original_count - len(self.employees)
        print(f"{deleted_emp} Employees Deleted!!!")

#  Find an employee by their name.

    def find_by_name(self, name):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                return emp
        return None

#  Update an employee's salary by name.

    def update_salary(self,name,new_salary):
        emp = self.find_by_name(name)
        if emp:
            emp.salary = new_salary
            print("Salary updated successfully...\n")
        else:
            print("No employee found\n")



