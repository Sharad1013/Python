# Problem
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# Twinkle, twinkle, little star,
# How I wonder what you are!

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Twinkle, twinkle, little star,
# How I wonder what you are!''')

# import pyttsx3

# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()



import os

# Specify the directory path or use the current directory
directory_path = input("Enter the Path")
# try:
    # List the contents of the directory
contents = os.listdir(directory_path)
print(f"Contents of '{os.path.abspath(directory_path)}':")
for item in contents:
    print(item)


# except FileNotFoundError:
#     print("Error: Directory not found.")
# except PermissionError:
#     print("Error: Permission denied.")
# except Exception as e:
#     print(f"An error occurred: {e}")
