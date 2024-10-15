from menu import Menu
class Restaurent():
    def __init__(self,name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self,employee):
        self.employees.append(employee)
    
    def view_employee(self):
        print("Employees list")
        for emp in self.employees:
            print(f"Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}, Address: {emp.address}, Age: {emp.age}, Designation: {emp.designation},Salary {emp.salary}")

