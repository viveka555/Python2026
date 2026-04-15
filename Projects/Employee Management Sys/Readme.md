#  Employee Management System (Python OOP)

##  Overview

The **Employee Management System** is a simple command-line application built using **Python and Object-Oriented Programming (OOP)** concepts.
It allows users to manage employee records efficiently through a menu-driven interface.

---

## 🚀 Features

* Add new employees
* View all employees
* Update employee salary
* Delete employees within an age range
* Search employee by name
* Prevent duplicate entries

---

## Project Structure

```
employee_system/
│
├── models/
│   └── employee.py
│
├── managers/
│   └── employees_manager.py
│
├── frontend/
│   └── frontend_manager.py
│
└── main.py
```

---

## 🧠 OOP Concepts Used

* **Encapsulation** → Employee data stored inside class
* **Abstraction** → Manager handles logic separately
* **Separation of Concerns** → UI, logic, and data are separated

---

## How It Works

### 1. Employee Class

Represents an individual employee:

* Name
* Age
* Salary
* Custom string representation using `__str__`

---

### 2. EmployeesManager Class

Handles all business logic:

* Add employee
* List employees
* Find employee
* Update salary
* Delete employees by age range

---

### 3. FrontEndManager Class

Provides CLI interface:

* Menu-driven system
* Takes user input
* Calls manager methods

---

## How to Run

1. Clone the repository or download files
2. Navigate to project folder
3. Run the program:

```bash
python main.py
```

---

## Sample Output

```
=== Employee System ===
1. Add Employee
2. List Employees
3. Delete by Age Range
4. Update Salary
5. Exit
=======================
```

---

# Common Issues & Fixes

### Issue: Employee not found

* Make sure employee is added before updating
* Avoid extra spaces → use `.strip()`

### Issue: Weird object output

* Ensure `__str__` method is implemented

---

##  Future Improvements

*  Save data using JSON or database
*  Add unique employee ID
*  Advanced search & filtering
*  Sorting (salary, age)
*  GUI version using Tkinter

---

## 🎯 Learning Outcomes

* Strong understanding of Python OOP
* Working with lists and objects
* Building CLI-based applications
* Writing clean and modular code

---

##  Author

Developed by **Vivek surale** 🚀

---

## License

This project is open-source and free to use for learning purposes.
