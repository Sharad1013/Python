# 1. Write a program using functions to find greatest of three numbers.
def goat(a,b,c):
    if(a > b and a > c):
        return a
    elif(b > c):
        return b
    else: 
        return c
    

# print(goat(45,55,64))


# 2. Write a python program using function to convert Celsius to Fahrenheit.

def conversion_To_C(fahrenheit):
    return 5 * (fahrenheit-32) / 9


# print(round(conversion_To_C(100),2), "C")

# 3. How do you prevent a python print() function to print a new line at the end.
# print("Anything", end="")
# print("Hello")

# 4. Write a recursive function to calculate the sum of first n natural numbers.
sum = 0
def sum_to_n(n):
    if (n == 1):
        return n
    
    return n + sum_to_n(n - 1)
# print(f"the sum of natural numbers is : {sum_to_n(5)}")


'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

def print_pattern(n):
    for i in range(1,n+1):
        print("* "*(n + 1 - i))
    
# print_pattern(5)

def print_pattern_with_recr(n):
    if( n == 0):
        return
    print("* " * n)
    print_pattern_with_recr(n - 1)
    
# print_pattern_with_recr(5)

# 6. Write a python function which converts inches to cms.
def inch_to_cm(inches):
    return inches * 2.54


# print(inch_to_cm(1))
# print(f"{inch_to_cm(5)} cm")

# 7. Write a python function to remove a given word from a list and strip it at the same time.


list = ["Sharad","Good","Boy","Rohan","Kanan","lalan","an"]

def removeList(list, word):
    new_list = []
    for item in list:
        if not(item == word):
            new_list.append(item.strip(word))
    return new_list
        
# print(removeList(list,"an"))

# Write a python function to print multiplication table of a given number.


def print_Table(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")


print_Table(5)
print_Table(10)
print_Table(15)