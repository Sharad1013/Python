# __INIT__() CONSTRUCTOR
"""
__init__() is a special method which is first run as soon as the object is created.
__init__() method is also known as constructor.
It takes ‘self’ argument and can also take further arguments.
"""

class Employee:
    # language = "Python"
    # salary = 450000

    def __init__(self,name,salary,language): # this is a special kind of method which automatically gets invoked as soon as the object is created.
        self.name = name
        self.salary = salary
        self.language = language

        print("I am creating an object")

    def getInfo(self):
        print(f"the salary is : {self.salary}")

    @staticmethod 
    def greet(self):
        print(f"Good morning")

# sharad = Employee()
# sharad.name = "sharad"
# print(sharad.name,sharad.salary)

# All the methods which starts with __ are called as dunder methods in python. 

# rohan = Employee()

# Modular Syntax

harry = Employee("Harry",1300000,"Java")
print(harry.name,harry.salary,harry.language)
