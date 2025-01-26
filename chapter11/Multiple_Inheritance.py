# Multiple Inheritance occurs when the child class inherits from more than one parent classes.

class Employee: # parent class, Base class
    company = "ITC"
    salary = 1000000
    def show(self):
        print(f"the name is {self.name} and, the salary is {self.salary}")

class Coder:
    lang = "python"
    def language(self):
        print(f"out of all the languages, your language is {self.lang}")

class Programmer(Employee,Coder):
    def food(self):
        print(f"The fav food for programmer is Bug")

Sharad = Programmer()
Sharad.name = "Sharad"
Sharad.food()
Sharad.language()
Sharad.show()

