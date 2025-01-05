# Strings Practice Set 


# Strings are immutable


# name = input("Enter the name : ")
# print(name + " Good Afternooon!!")
# print(f"Good Afternoon!! {name}") # fStrings


# Question 2
# letter = ''' Dear <|Name|>, You are selected! <|Date|>'''

# print(letter.replace("<|Name|>","Sharad").replace("<|Date|>","5th jan")) # will return a string

# this is called chaining ( Done above )



# Question 3 
name = "Sharad is alone  and going to be successful."
print(name.find("  ")) # the find function finds any of the given provided substring in the string. it returns the occurence of the substring in the parent string. 

# Question 4
print(name.replace("  ", " "))


# Question 5
letter = "Dear Harry,\n\t This python course is nice.\nThanks!"

print(letter);