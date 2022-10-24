# Inheritance, Extending, Overriding

# Parent Class
class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")

# Child Class #1
class SoftwareEngineer(Employee): # Put in parent class to inherit from it
    
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary) # Inherits (name, age) from parent class
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging...")

    def work(self):
        print(f"{self.name} is coding...") # Overrides the parent class
        
# Child Class #2
class Designer(Employee):
    
    def draw(self):
        print(f"{self.name} is drawing...")

    def work(self):
        print(f"{self.name} is designing...")


se1 = SoftwareEngineer("Max", 23, 6000, "Junior")
se2 = SoftwareEngineer("Lisa", 30, 9000, "Senior")
d1 = Designer("Philip", 27, 7000)

# Polymorphism

employees = [se1, se2, d1]

def motivate(employees):
    for employee in employees:
        employee.work()

motivate(employees)

