# 1. Write a program to print multiplication table of a given number using for loop.

# number = int(input("Enter the number : "))

# for i in range(1, 11):
#     print(f"{number} X {i} = {number * i} ")

# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for i in l:
#     if(i.startswith("S")):
#         print(f"Good night!! {i}")

# 3.Attempt problem 1 using while loop.
# number = int(input("Enter the number: "))
# i = 1
# while(i <= 10):
#     print(f"{number} X {i} = {number * i}")
#     i+=1

# 4. Write a program to find whether a given number is prime or not.

# isPrime = True
# number = int(input("Enter the number: "))

# for i in range(2, number):
#     if(number % i == 0):
#         isPrime = False
#         break
#     else:
#         isPrime = True

# print(isPrime)


# 5. Write a program to find the sum of first n natural numbers using while loop.

# number = int(input("Enter the number: "))
# sum = 0
# i = 1
# while(i <= number):
#     sum = sum + i
#     i = i + 1
# print(sum)

# 6. Write a program to calculate the factorial of a given number using for loop.
# number = int(input("Enter the number: "))
# fact = 1
# for i in range(1, number+1):
#     fact = fact * i

# print(f"factorial of {number} is {fact}")

# 7. Write a program to print the following star pattern.
'''
  *
 ***
*****
for n = 3 

'''
# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     # spaces
#     print(" " * (n - i), end = "")
#     print("*" * (2*i-1), end = "")
#     print("")



# 8. Write a program to print the following star pattern: 
'''
*
**
*** for n = 3

'''

# for i in range(1,n+1):
#   print("*"*i)



# 9. Write a program to print the following star pattern.
''' 
* * *
*   * for n = 3
* * *  
'''

# for i in range(1, n + 1):
#   if(i == 1 or i == n):
#     print ("*" * n)
#   else:
#     print("*",end="")
#     print(" "* (n-2),end="")
#     print("*",end="")
#     print("")


# 10. Write a program to print multiplication table of n using for loops in reversed order.cls


# i = 10
# while(i >= 1):
#   print(f"{n} X {i} = {n * i}")
#   i-=1


num = 5
for i in range(1,11):
  print(f"{num} * {11 - i} = {(num) * (11-i)}")