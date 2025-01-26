# Class Methods -->> This is the way using which we can access the classes inside a method. 

# class Employee:
#     a = 1
#     def show(self):
#         print(f"The class value of a is {self.a}")
class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

e = Employee()
e.a = 45
print(e.a)


e.show() # 45 as self shows the attribute of the instance but when used the @classmethod it will access the class attribute a. 


# So now the thing is that we want to access the Class attribute value not the instance attribute value so for that we can use @classmethod decorator same like @staticmethod. The class method uses cls instead of self 
# Self means the object on which that method is running
# cls means the class of that object on which the method is running. 

