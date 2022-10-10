# Class
class SoftwareEngineer:
    
    # Class Attributes
    alias = "Keyboard Magician"
    access_level = 5

    def __init__(self, name, age, level, salary):
        # Instance Attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # Functions in Classes: Instance Method
    def code(self):
        print(f"{self.name} is writing code...")

    def code_language(self, language):
        print(f"{self.name} is writing code in {language}")


    # def information(self):
    #     print(f"Name: {self.name}")
    #     print(f"Age: {self.age}")
    #     print(f"Level: {self.level}")

    # Functions in Classes: Dunder Method
    def __str__(self): # Calls this function whenever object is converted to a string
        information = (f"Name: {self.name}\nAge: {self.age}\nLevel: {self.level}")
        return information

    def entry_salary(age): # Function will only work on SoftwareEngineer class eg. print(SoftwareEngineer.entry_salary())
        if age < 25:
            return 5000
        if age <30:
            return 7000
        return 9000


# Instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
se2 = SoftwareEngineer("Lisa", 22, "Senior", 7000)

print(SoftwareEngineer.entry_salary(25))