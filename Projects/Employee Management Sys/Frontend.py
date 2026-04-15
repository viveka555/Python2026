from Emp_Manager import EmployeeManager

class FrontendManager:

    def __init__(self):
        self.manager = EmployeeManager()
        self.menu()

    def menu(self):
        while True:
            print("========Employee System========")
            print("1. Add new employee")
            print("2. list employees")
            print("3. Delete employee by age range")
            print("4. Update salary by name")
            print("5. To exit the menu")
            print("===============================")

            choice = input("Enter your choice:")

            if choice == "1":
                name = input("Enter employee name:")
                age = input("Enter employee age:")
                salary = input("Enter employee salary:")
                self.manager.add_employee(name, age, salary)

            elif choice == "2":
                self.manager.list_employee()

            elif choice == "3":
                min_age = input("Enter min_age of employee:")
                max_age = input("Enter max_age of employee:")
                self.manager.delete_emp_by_age_range(min_age,max_age)

            elif choice == "4":
                name = input("Enter employee name:")
                new_salary = float(input("Enter new salary:"))
                self.manager.update_salary(name ,new_salary)

            elif choice == "5":
                print("Exiting the Menu...")
                break

            else:
                print("Invalid choice entered!!!!\n")
        