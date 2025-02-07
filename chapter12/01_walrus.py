                                # WALRUS OPERATOR
# The walrus operator (:=), introduced in Python 3.8, allows you to assign values to variables as part of an expression. This operator, named for its resemblance to the eyes and tusks of a walrus, is officially called the "assignment expression."

# Using walrus operator

"""if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") """

# Output: List is too long (5 elements, expected <= 3)


# if(num := 1+2 > 2):
#     print(num)


# Type Definitions in python
# Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.

n : int = 5
name : str = "Sharad"

# in functions
def sum(a : int,b : int) -> int: # means it will take two arguments a as int, b as int and will return the sum as int ( a + b )
    return a + b

