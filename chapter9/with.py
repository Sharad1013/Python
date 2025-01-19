# With statement for file Input and Output



# Reading the file

# file = open("read_file.txt")
# read_file = file.read()
# print(read_file)

# file.close()


# Using this there is no need to explicitly close the file


with open("read_file.txt") as file:
   print(file.read())
# No need to close the file over here.

