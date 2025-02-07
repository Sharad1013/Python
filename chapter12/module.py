""" 

IF __NAME__== ‘__MAIN__’ IN PYTHON

‘__name__’ evaluates to the name of the module in python from where the program is ran.
If the module is being run directly from the command line, the ‘ __name__’ is set to string “__main__”. Thus, this behaviour is used to check whether the module is run directly or imported to another file.

"""

def myFunc():
    print("Hello world")

# myFunc()
# print(__name__) # will print the origin from where the file has been imported and if it prints main it means that you are executing the code in the same file which is its origin also

if __name__ == "__main__":
    # If this code is executed by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)