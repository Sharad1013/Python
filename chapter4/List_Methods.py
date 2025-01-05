friends = ["Apple","Orange",3.2, 1,5]

# List Methods
# All the String methods used to return a new String so it was needed to print them but not with lists.
# print(friends)
# friends.append("Sharad")
# print(friends)

l1 = [1,2,3,6,5,4,7,9,44]

# l1.sort()
# l1.reverse()

# Append adds the item in the end of the list but insert inserts it at the specified index
l1.insert(3, 3333) # Insert 3333 before 3rd index
print(l1.pop()) # if not specified any index will pop from the end else pop the element at the given index
# remove method removes the specified value from the list.
print(l1)

l1.remove(6)

print(l1)