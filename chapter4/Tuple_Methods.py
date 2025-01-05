tup = (1,2,3,442,5,7,"Rohan","Shivam",False)

no = tup.count(5)
# print(no)


i = tup.index(442)
# print(i)

tup1 = (1,2,3)
tup2 = (4,5,6)

concatenated = tup1 + tup2
# print(concatenated)

# print(concatenated * 3)
repeated = tup1 * 3
# print(repeated)

print(len(tup1))


print(2 in tup1)


# Unpacking my tuple
a,b,c = tup1

print(f"{a},{b},{c}")

# Slicing in Tuple 

print(repeated[1:4])