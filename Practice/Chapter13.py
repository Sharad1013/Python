# 1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one? done in cmd
"""Done"""

# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:
# name = input("Enter your name : ")
# number = int(input("Enter your number : "))
# marks = int(input("Enter your marks : "))

""" “The name of the student is Harry, his marks are 72 and phone number is 99999888” """
# Sharad = "The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,number)

# print(Sharad)


# 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

table = [str(7 * i) for i in range(1,11)]

s = "\n".join(table)

# print(s)


# 4. Write a program to filter a list of numbers which are divisible by 5.

def divisible_by_5(n):
    if(n % 5 == 0):
        return True
    return False

# li = [5,10,15,16,17,20,25,24,65]

# list2 = list(filter(divisible_by_5,li))
# print(list2)

# 5. Write a program to find the maximum of the numbers in a list using the reduce function.
li = [5,10,15,16,17,20,25,24,65]

def greater(a,b):
    if(a > b):
        return a
    return b

from functools import reduce

# print(reduce(greater,li))

# 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.
"""Done"""

