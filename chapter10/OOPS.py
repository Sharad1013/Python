# Solving a problem by creating object is one of the most popular approaches in programming. This is called object-oriented programming. This concept focuses on using reusable code (DRY Principle).


"""Class"""
# A class is a blueprint for creating object.


# Creating a class
class Employee:
    # name = "Sharad"
    language = "Python"
    salary = 450000

    def getInfo(self):
        print(f"the salary is : {self.salary}")

    def greet(self):
        print(f"Good morning")


sharad = Employee()
sharad.name = "sharad"

print(sharad.language)
# sharad.getInfo()  == Employee.getInfo(sharad)
"""
An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation.

Objects of a given class can invoke the methods available to it without revealing the implementation details to the user. – Abstractions & Encapsulation!

"""
# class attributes
# An attribute that belongs to the class rather than a particular object.
print(sharad.language, sharad.salary, sharad.name)





rohan = Employee()
rohan.name = "rohan"
print(rohan.salary, rohan.language, rohan.name)

# Here name is object attribute and the salary and language are class attributes as they belong to the class.

" An attribute that belongs to the Instance (object). --> Object Atrribute and instance attribute are same "

"""
Note: Instance attributes, take preference over class attributes during assignment & retrieval.
"""

rohan.name = "rohan"
rohan.language = "javaScript"
print(rohan.salary, rohan.language, rohan.name)

# 
"""When looking up for sharad.attribute it checks for the following:
1) Is attribute present in object?
2) Is attribute present in class?
"""

# __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also known as constructor.
# It takes ‘self’ argument and can also take further arguments.
