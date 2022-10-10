# Encapsulation (make private) & Abstraction

class SoftwareEngineer:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None # '_' keeps the instance attribute private
        self._num_bugs_solved = 0

    def get_salary(self):
        return self._salary

    def set_salary(self, value):
        self._salary = value

    def code(self):
        self._num_bugs_solved += 1

se1 = SoftwareEngineer("Max", 25)

se1.set_salary(6500)
print(se1.get_salary())
