class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age) # calling the parent class constructor
        self.employee_id = employee_id
        
# Creating an Employee object
emp = Employee("Alice", 30, "E12345")
print(f"Name: {emp.name}, Age: {emp.age}, ID: {emp.employee_id}")