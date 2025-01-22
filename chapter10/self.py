# Self Parameter

class Employee:
    language = "Python"
    salary = 450000

    def getInfo(self):
        print(f"the salary is : {self.salary}")

    @staticmethod 
    def greet(self):
        print(f"Good morning")

sharad = Employee()
sharad.name = "sharad"
sharad.salary = 1200000
sharad.getInfo()
sharad.greet()

rohan = Employee()
rohan.name = "rohan"
rohan.getInfo()

# sharad.getInfo() == Employee.getInfo(sharad) -->> This self argument is the one which accepts this argument sharad into it.


# STATIC METHOD
"Sometimes we need a function that does not use the self-parameter. We can define a static method like this:"

# for example : in the above case i am passing the whole sharad object to the greet function while it is not even needed. so instead of that i can make this greet method as a static method using the @staticmethod keyword. this means that the greet method is a decorator and does not require object. 



