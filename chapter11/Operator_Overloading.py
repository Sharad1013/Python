# OPERATOR OVERLOADING IN PYTHON
# Everything in python is a class

"""
Operators in Python can be overloaded using dunder methods.
These methods are called when a given operator is used on the objects.
"""



class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num): # Overloading the + operator
        return self.n + num.n 

n = Number(2)
m = Number(4)

print(n + m) # This will throw an error. so in python if we want we can customise the operations happening on any operands. like in this case we can customise the add operator