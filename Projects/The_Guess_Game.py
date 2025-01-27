"""
                                    ROJECT 2 – THE PERFECT GUESS
We are going to write a program that generates a random number and asks the user to guess it.
If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
Hint: Use the random module.

"""

from random import randint

random_number = randint(1,11) # Number to Guess
def guess(random_number):
    retries = 1
    while(True):
        user_choice = int(input("Enter your choice!! "))
        if(user_choice < random_number):
            print(f"try higher number please!!")
        elif(user_choice > random_number):
            print(f"try lower number please!!")
        else:
            print(f"Congrats you got it in {retries} tries, the number is {random_number}")
            break
        retries += 1

guess(random_number)



