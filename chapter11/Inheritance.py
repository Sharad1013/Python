# CHAPTER 11 - INHERITANCE & MORE ON OOPS
# Inheritance is a way of creating a new class from an existing class.

class Employee: # parent class, Base class
    company = "ITC" # Property
    salary = 1000000
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
    
"""class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

    def showlanguage(self):
        print(f"The name is {self.name} and knows {self.language} language")"""

# Inheritance

class Programmer(Employee): # derived class, Child class
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and knows {self.language} language")


a = Employee()
a.name = "Sharad"
b = Programmer()
b.name = "Shravan"

print(a.show(), b.show())

"""
TYPES OF INHERITANCE
• Single inheritance
    Single inheritance occurs when child class inherits only a single parent class.


• Multiple inheritance
    Multiple Inheritance occurs when the child class inherits from more than one parent classes.

• Multilevel inheritance
    When a child class becomes a parent for another child class.

"""
