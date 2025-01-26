# When a child class becomes a parent for another child class.

class Employee: # parent class, Base class
    company = "ITC"
    salary = 1000000
    def show(self):
        print(f"the name is {self.company} and, the salary is {self.salary}")

class Coder(Employee):
    lang = "python"
    def language(self):
        print(f"out of all the languages, your language is {self.lang}")


class Programmer(Coder):
    domain = "LLM"
    def program(self):
        print(f"Making the script for domain {self.domain}")


Sharad = Programmer()
Sharad.show()
Sharad.program()
Sharad.language()


# Super Method
# super() method is used to access the methods of a super class in the derived class.


