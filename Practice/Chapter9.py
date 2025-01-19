# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

# with open("poems.txt") as poem_file:
#     # print(poem_file.read())
#     if ("wonder" in poem_file):
#         print("found the word !!")
#     else:
#         print("did not found the word !!")


# file = open("poems.txt")
# content = file.read()

# if("twinkle" in content):
#     print("found the word!!")
# else:
#     print("word is not present")

# file.close()


# 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

# import random

# def game():
#     print("you are playing the game..")
#     score = random.randint(1,62)
#     with open("Hi_Score.txt") as hiScore:
#         high_score = hiScore.read()
#         if(high_score != ""):
#             high_score = int(high_score)
#         else:
#             high_score = 0

#     print(f"Your score is : {score}")

#     if(score > high_score):
#         # write this score to file
#         with open("Hi_Score.txt","w") as f:
#             f.write(str(score))
#     return score


# game()

# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.


# def generate_table(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n * i}\n"

#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write(table)


# for i in range(2,21):
#     generate_table(i)
        


# 4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

# with open("Donkey.txt","r") as donkey_file:
#     content = donkey_file.read()

#     contentNew = content.replace("Donkey","#####")

# with open("Donkey.txt","w") as donkey_file:
#     donkey_file.write(contentNew)
        


# 5. Repeat program 4 for a list of such words to be censored.

# cuss_word = ["hello", "how", "bad"]

# with open("Donkey.txt","r") as donkey_file:
#     content = donkey_file.read()

# for i in cuss_word:
#     content = content.replace(i,"#" * len(i))

# with open("Donkey.txt","w") as donkey_file:
#     donkey_file.write(content)



# 6. Write a program to mine a log file and find out whether it contains ‘python’.

# with open("log.txt","r") as log_file:
#     log_file_content = log_file.read()
#     if("python" in log_file_content):
#         print("found it")
#     else:
#         print("not present") 



# 7. Write a program to find out the line number where python is present from ques 6.


# with open("log.txt","r") as log_file:
#     lines = log_file.readlines()

# line_no = 1
# for line in lines:
#     if("python" in line):
#         print(f"found python in {line_no}")
#         break
#     line_no += 1
# else:        
#     print("not present") 


# 8. Write a program to make a copy of a text file “this.txt”
# with open("this.txt","r") as text_file:
#     text_file_content = text_file.read()


# with open("this_copy.txt","w") as text_copy:
#     text_copy.write(text_file_content)



# 9. Write a program to find out whether a file is identical & matches the content of another file.

# with open("this.txt","r") as text_file:
#     text_file_content = text_file.read()
# with open("this_copy.txt","r") as text_file:
#     text_copy_file_content = text_file.read()


# if(text_file_content == text_copy_file_content):
#     print("copied")
# else:
#     print("not copied")


# 10. Write a program to wipe out the content of a file using python.

# with open("old.txt","w") as text_file:
#     text_file.write("")


# 11. Write a python program to rename a file to “renamed_by_ python.txt.


with open("old.txt","r") as old_text_file:
    old_text_file_content = old_text_file.read()

with open("renamed_by_python.txt","w") as renamed_by_python:
    renamed_by_python.write(old_text_file_content)
