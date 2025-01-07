marks = {
    "Sharad": 100,
    "Shubham": 55,
    "Rohan":50,
    "list" : [1,2,3]
}


# print(marks.items())

# print(marks.keys())
# print(marks.values())

marks.update({"Sharad":99, "Ruhi" : 98})
# print(marks)


print(marks.get("Sharad"))
print(marks["Sharad"])

# Difference between print(marks.get("Sharad")) and print(marks["Sharad"])

'''
but the real difference lies in the condition where we want to access any key which is not present in the dictionary. like 
print(marks.get("Shivika)) -->> this will print None as Shivika is not a key in the dictionary. 
print(marks["Shivika]) -->> but this will return an error if Shivika is not a key in the dictionary.

'''

