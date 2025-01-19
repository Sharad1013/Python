
print("Scraping the file!!")

# Reading the file

# file = open("read_file.txt")
# read_file = file.read()
# print(read_file)

# file.close()


# Writing the file

# str = "You are gonna make it!!"

# file = open("read_file.txt","w")


# file.write(str)

# file.close()

# Append mode 


f = open("read_file.txt", "a")
# lines = f.readline()

lines_to_append = f.write("\nThis is appended!!")
print(lines_to_append)
f.close()
# 6:00:11

