# Property Decorators 

class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")
    # Property decorator
    @property
    # The method name with ‘@property’ decorator is called getter method.
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    # We can define a function + @ name.setter decorator like below:
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        # The above will return a list of name

e = Employee()
# e.a = 45
e.name = "Sharad Sinha"

# print(e.name)
print(e.fname, e.lname)
# print(e.a)
# e.show()