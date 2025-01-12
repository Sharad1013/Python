'''
A function is a group of statements performing a specific task.

When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!

A function can be reused by the programmer in a given program any number of times. '''


def avg(): # function definition
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    num3 = int(input("Enter the third number : "))
    print((num1 + num2 + num3)/3)

# avg() # function call
# print("Done")

# Quick Quiz: Write a program to greet a user with “Good day” using functions.

def greet():
    user = input("Enter the user name : ")
    print(f"Good day {user}")

# greet()

def greet(user):
    # user = input("Enter the user name : ")
    print(f"Good day {user}")

# greet("sharad")
# greet("Amber")



# function can return something

def greet(user):
    # user = input("Enter the user name : ")
    # print(f"Good day {user}")
    return "done"

# returned_val = greet("Sharad")

# print(returned_val)


# Default Parameter


def greet(user = "user1"):
    # user = input("Enter the user name : ")
    print(f"Good day {user}")
    return "done"

greet()
greet("sharad")