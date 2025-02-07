# MAP, FILTER & REDUCE
# Map applies a function to all the items in an input_list.
# Syntax.
li = [1,2,3,4,5]

square = lambda x : x * x
sq_list = map(square,li)
# print(list(sq_list))

# map(function, input_list) 
    # the function can be lambda function

# Filter creates a list of items for which the function returns true.
def even(n):
    if( n % 2 == 0):
        return True
    return False

onlyEven = filter(even,li)
# print(list(onlyEven))


# reduce function
def sum(a,b):
    return a + b


def mul(a,b):
    return a * b

from functools import reduce

# reduce needs to be imported from the func tool module
print(reduce(sum,li)) # 15 -->> will run the function sum with two arguments at a time of li
print(reduce(mul,li)) # 120