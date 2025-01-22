# Creating a class
class Employee:
    language = "Python"
    salary = 450000

    def getInfo(self):
        print(f"the salary is : {self.salary}")

    def greet(self):
        print(f"Good morning")

sharad = Employee()
sharad.name = "sharad"
sharad.language = "javaScript"

rohan = Employee()
rohan.name = "rohan"
rohan.language = "Java"


print(sharad.name,sharad.language,sharad.salary) # sharad javaScript 450000
print(rohan.name,rohan.language,rohan.salary) # rohan java 450000

# Because the instance attributes take prefrence over the class values.

"""
When looking up for harry.attribute it checks for the following:
1) Is attribute present in object?
2) Is attribute present in class?
"""