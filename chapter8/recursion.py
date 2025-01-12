'''
                    RECURSION
    Recursion is a function which calls itself.
It is used to directly use a mathematical formula as function 

'''
def factorial(n):
    # Base Case
    if(n == 1 or n == 0):
        return 1
    
    return n * factorial(n - 1)

# print(factorial(5))
# print(factorial(7))

'''The programmer needs to be extremely careful while working with recursion to ensure that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most direct way to code an algorithm.'''