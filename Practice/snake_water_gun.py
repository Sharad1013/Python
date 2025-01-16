# snake,water and gun

import random
import math
pc_moves = ["snake","water","gun"]
pc_choice = pc_moves[math.floor(random.random() * 3)]
print(pc_choice)

user_choice = input("Enter the choice (snake, water, gun :  )")

def win_move():
    # Tie
    if(pc_choice == user_choice):
        print(f"the pc choice is {pc_choice} & user choice is {user_choice} so Tie")
    # pc_won moves
    if((pc_choice == "snake".lower()) and (user_choice == "water".lower())):
        print(f"the pc_choice is {pc_choice} and the user_choice is {user_choice} so pc won")
    elif((pc_choice == "water".lower()) and (user_choice == "gun".lower())):
        print(f"the pc_choice is {pc_choice} and the user_choice is {user_choice} so pc won")
    elif((pc_choice == "gun".lower()) and (user_choice == "snake".lower())):
        print(f"the pc_choice is {pc_choice} and the user_choice is {user_choice} so pc won")
    else:
        print(f"the pc_choice is {pc_choice} and the user_choice is {user_choice} so user won")

win_move()



