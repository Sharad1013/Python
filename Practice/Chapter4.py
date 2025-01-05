# 1. Write a program to store seven fruits in a list entered by the user.

# fruits = []


# for i in range(0,7): 
#     i = input(f"Enter the fruit no. {i + 1} in List: ")
#     fruits.append(i)


# print(fruits)

# Write a program to accept marks of 6 students and display them in a sorted manner.

# marks = [] 

# for i in range(0,6):  #( if want it to end at 6 write 0,7 as last one is excluded )
#     i = int(input(f"Enter the marks no. {i + 1} in List: "))
#     marks.append(i)

# marks.sort()
# print(marks)


# 3. Check that a tuple cannot be modified in python.
tup = (1,2,3,442,5,7,"Rohan","Shivam",False)
# tup[3] = 123 Error
# list = [tup]
# print(type(tup))



# 4. Write a program to sum a list with 4 numbers.
list = [1,2,3,4,5]
# print(len(list))
# optimizedSum = int(max(list) * ((max(list) + 1)) / 2)
optimized = int(max(list) * ((max(list) + 1)/2))
# print(optimized)

#  inbuilt
# print(sum(list))
# sum = 0
# for i in list:
#     sum += i

# print(sum) 
# print(optimizedSum)


# Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)

print(a.count(0))