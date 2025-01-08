# Sometimes we want to play PUBG on our phone if the day is Sunday.
# Sometimes we order Ice Cream online if the day is sunny.
# Sometimes we go hiking if our parents allow.
# All these are decisions which depend on a condition being met.
# In python programming too, we must be able to execute instructions on a condition(s) being met.
# This is what conditionals are for!


age = int(input("Enter your num: "))

# If else
# if(age >= 18):
#     print("you are eligible!!")
#     print("Good For You")
# else :
#     print("Not eligible")
#     print("Chal Nikal")

# Multiple Conditions
# If elif else ladder
if(age >= 18):
    print("you are eligible!!")
    print("Good For You")

elif (age < 0):
    print("Enter a Valid Age!!!!")

elif (age == 0):
    print("Entered 0!!")

else:
    print("Not eligible")
    