# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = {
    "ladka" : "Boy",
    "ladki": "girl",
    "phul":"flower",
    "billi":"cat",
}

lookUp = input("Enter the word : ")
print(words[lookUp])


# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
# s = set()
# for i in range(0,8):
#     user_input = int(input(f"Enter the Numbers {i + 1} : "))
#     s.add(user_input)

# print(s)

# 4. What will be the length of following set s:  --> 2 ( because python does not cares about data type when using == operator so 20 and 20.0 are same)
s = set() 
s.add(20) 
s.add(20.0)
s.add('20') 
print(s)
print(len(s))



#5. What is the type of 's'? -->> tuple
# s = {}
# print(type(s))


#6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

language = {};

for i in range(1,5):
    user_input = input("Enter your name: ")
    lang = input("Enter language name:  ")
    # language.update({lang : user_input})
    language.update({user_input : lang})

print(language)


# 7. If the names of 2 friends are same; what will happen to the program in problem 6? -->> it will update the value of the existing one in the dictionary

# 8 If languages of two friends are same; what will happen to the program in problem 6? -->> nothing values can be duplicate. keys needs to be unique but not values

# 9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]}
    #  -->> a. it can not be done as we cant access the elements present inside the set as it is not indexed.
    # b. We can't put a list inside a set. 