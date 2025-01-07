s1={1,2,3,78}
s2 = {7,8,1,78}

# Union -->> take all the data present in both the sets
print(s1.union(s2)) # {1, 2, 3, 7, 8, 78}

# Intersection -->> takes the common values only from both the sets
print(s1.intersection(s2)) # {1,78}
