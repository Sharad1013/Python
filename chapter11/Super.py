# When a child class becomes a parent for another child class.

class Employee: # parent class, Base class
    company = "ITC"
    def __init__(self):
        print("Constructor Called!! Employee")
    # salary = 1000000
    def show(self):
        print(f"the name is {self.company} and, the salary is {self.salary}")

class Coder(Employee):
    lang = "python"
    def __init__(self):
        print("Constructor Called!! Coder")
    def language(self):
        print(f"out of all the languages, your language is {self.lang}")


class Programmer(Coder):
    domain = "LLM"
    def __init__(self):
        super().__init__() # here the super method will call the constructor of the parent of current class i.e coder. 
        print("Constructor Called!! Programmer")
    # def program(self):
    #     print(f"Making the script for domain {self.domain}")


# Super Method
# super() method is used to access the methods of a super class in the derived class.


Sharad = Programmer()


