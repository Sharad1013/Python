# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
# class Programmer:
#     company = "Microsoft"
#     def __init__(self,name,role,salary):
#         self.name = name
#         self.role = role
#         self.salary = salary


# sharad = Programmer("Sharad","Data Scientist","120000")

# print(sharad.name, sharad.role, sharad.salary)

# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

# class Calculator:
#     def __init__(self,number):
#         self.number = number

#     def square(self):
#         print(f"square : {self.number * self.number}")
    
#     def cube(self):
#         print(f"cube : {self.number * self.number * self.number}")

#     def square_root(self):
#         print(f"square root : {self.number ** 1/2}")
    
# num1 = Calculator(4)

# num1.square()
# num1.cube()
# num1.square_root()

# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

# class ques_3:
#     # Class attribute
#     a = 3

# question_3 = ques_3()

# print(question_3.a)

# # this changes the instance attribute not the class attribute
# question_3.a = 0

# # so if you print the class attribute, it remains the same

# # print (ques_3.a)

# print(question_3.a)


# 4. Add a static method in problem 2, to greet the user with hello.

# class Calculator:
#     def __init__(self,number):
#         self.number = number

#     def square(self):
#         print(f"square : {self.number * self.number}")
    
#     def cube(self):
#         print(f"cube : {self.number * self.number * self.number}")

#     def square_root(self):
#         print(f"square root : {self.number ** 1/2}")

#     @staticmethod
#     def greet():
#         print("Hello there!!")
    
# num1 = Calculator(4)

# num1.square()
# num1.cube()
# num1.square_root()
# num1.greet()

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

# from random import randint

# class Train:

#     def __init__(self,train):
#         self.train = train

#     def book_ticket(self,fro,to):
#         print(f"Ticket is booked in train no: {self.train} from {fro} to {to}")

#     def get_status(self):
#         print(f"Train no : {self.train} is running on time")
#         pass

#     def getFare(self,fro,to):
#         print(f"Ticket fare in train no: {self.train} from {fro} to {to} is {randint(222,5555)}")


# t = Train(12399)
# t.get_status()
# t.book_ticket("rampur","jaipur")

# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.


from random import randint

class Train:

    def __init__(slf,train):
        slf.train = train

    def book_ticket(slf,fro,to):
        print(f"Ticket is booked in train no: {slf.train} from {fro} to {to}")

    def get_status(slf):
        print(f"Train no : {slf.train} is running on time")
        pass

    def getFare(slf,fro,to):
        print(f"Ticket fare in train no: {slf.train} from {fro} to {to} is {randint(222,5555)}")


t = Train(12399)
t.get_status()
t.book_ticket("rampur","jaipur")

# No issue just maintain consistency -->> it is just a good practice to use self