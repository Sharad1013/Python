# EXCEPTION HANDLING IN PYTHON
"""
There are many built-in exceptions which are raised in python when something goes wrong.

Exception in python can be handled using a try statement. The code that handles the exception is written in the except clause.

"""

# try: 
#     # Code which might throw exception 
#     entry = input("enter your name: ")
#     print(entry + "sharad")
# except Exception as error: 
#     print(f"{error}")

''' 
When the exception is handled, the code flow continues without program interruption.
'''

# We can also specify the exception to catch like below:

# try:
#     # Code 
#     entry = input("enter your name: ")
#     print(entry)
# except ZeroDivisionError: 
#     # Code 

# except TypeError: 
#     # Code 
# except ValueError as v:
#     #code
#     print(f"ValueError{v}")
# except: 
    # Code 
# All other exceptions are handled here.


# Raising Exception
try:
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
    if(b == 0):
        raise ZeroDivisionError("you cant divide by 0") # raising the error
    else: 
        print(f"The division a/b is {a/b}")
except Exception as e:
    print(e)
