# a = 89
# def func():
    # global a # will change the global a only
    # a = 3
    # print(a) # 3

# func()
# print(a) # 3


# THE GLOBAL KEYWORD
# ‘global’ keyword is used to modify the variable outside of the current scope.

# Enumerate function in python
# The ‘enumerate’ function adds counter to an iterable and returns it

# list = [2,33,513,53,55]
# index = 0

# for item in list:
#     index += 1
#     print(f"The item number {index} is {item}")

# This can be simplifies using enumerate function
# for index, item in enumerate(list):
#     print(f"The item number {index} is {item}")


# LIST COMPREHENSIONS
# List Comprehension is an elegant way to create lists based on existing lists.


list1 = [1,7,12,11,22]
# squared_list = []
# for item in list1:
#     squared_list.append(item * item)
# print(squared_list)

list2 = [item*item for item in list1 if item >= 11]

print(list2)
