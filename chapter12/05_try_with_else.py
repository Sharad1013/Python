# TRY WITH ELSE CLAUSE
# Sometimes we want to run a piece of code when try was successful.

# try:
#     a = int(input("Enter the number : "))
#     print(a)
# except Exception as e:
#     print(e)

# else: # control will only enter here if the try block is executed successfully
#     print("I am inside else")


# Try with finally
# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of the exception.

# try:
#     a = int(input("Enter the number : "))
#     print(a)
# except Exception as e:
#     print(e)

# finally:
#     print("I am inside finally")

# Note the issue is that in normal try/except block finally works same as normal print statements. but the real difference occurs when we use it within a function.


def main():
    try:
        a = int(input("Enter the number : "))
        print(a)
        return a
    except Exception as e:
        print(e)
        return e
    finally:
        print("I am inside finally within the function")

main()

# So the real difference over here is that even if we return the value from the try block still it will go to the finally block and execute that also which is not possible with the normal print statements.



