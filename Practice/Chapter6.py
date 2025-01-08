# 1. Write a program to find the greatest of four numbers entered by the user.
'''
num1 = int(input("Enter num 1 : "))
num2 = int(input("Enter num 2 : "))
num3 = int(input("Enter num 3 : "))
num4 = int(input("Enter num 4 : "))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print(f"{num1} is greatest")
elif(num2 > num3 and num2 > num4):
    print(f"{num2} is greatest")
elif(num3 > num4):
    print(f"{num3} is greatest")
else:
    print(f"{num4} is greatest")
    
'''


# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

# maths = int(input("Enter marks for maths : "))
# english = int(input("Enter marks for english : "))
# hindi = int(input("Enter marks for hindi : "))


# Check for total percentage > 40 -->> pass
# total_percentage = (100 * (maths + english + hindi)) / 300

# if(total_percentage >= 40 and maths >= 33 and english >= 33 and hindi >= 33):
#     print("Congrats you pass!!")
# else:
#     print("Better Luck next time!!")

# print(f"{total_percentage} total percentage!" )


# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# comment = input("Enter the comments: ")

# if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
#     print("Spam Alert!!")
# else:
#     print("Good to go!!").

# 4. Write a program to find whether a given username contains less than 10 characters or not.
# username = input("Enter username : ")

# if(len(username) < 10):
#     print("username contains less than 10 characters!!")
# else:
#     print("good to go")


# 5. Write a program which finds out whether a given name is present in a list or not.

# list = []
# for i in range(0,2):
#     name = input("Enter your name: ")
#     list.append(name)

# check_name = input("Enter the nameCheck: ")
# if(check_name in list):
#     print("got it!!")
# else:
#     print("N/A")


# 6. Write a program to calculate the grade of a student from his marks from the following scheme: 
''' 
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 => C
50 – 60 => D 
< 50 => F
'''

# marks = int(input("Enter the marks : "))

# if(marks <= 100 and marks >= 90):
#     grade = "Ex"
# elif(marks < 90 and marks >= 80):
#     grade = "A"
# elif(marks < 80 and marks >= 70):
#     grade = "B"
# elif(marks < 70 and marks >= 60):
#     grade = "C"
# elif(marks < 60 and marks >= 50):
#     grade = "D"
# else:
#     grade = "F"

# print(grade)


# 7. Write a program to find out whether a given post is talking about “Harry” or not.
post = input("Enter the post: ")

if("Harry".lower() in post.lower()):
    print("Post About Harry!!")

else:
    print("Not talking about Harry!!")