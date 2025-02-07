# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

with ( open("1.txt") as one, open("2.txt") as two, open("3.txt") as three ) :
    print(one.read())
    print(two.read())
    print(three.read())

# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

list1 = [1,2,3,4,5,6,7,8]

for i,item in enumerate(list1):
    if(i == 2 or i == 4 or i == 6):
        print(item)

# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

n = int(input("Enter the number : "))
table = [n*i for i in range(1,11)]
print(table)


# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
try:
    a = int(input("enter the number : "))
    b = int(input("Enter the second number : "))
    print(a/b)
except ZeroDivisionError as e:
    print(f"exception {e}")

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter the number : "))
list2 = [n*i for i in range(1,11)] # will print the table

with open ("Tables.txt","a") as table:
    for items in list2:
        table.write(str(items) + "\n")
