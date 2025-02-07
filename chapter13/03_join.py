# JOIN METHOD (STRINGS)
# Creates a string from iterable objects.

list = ["sharad","harry","rohan"]
final = "-".join(list) # sharad-harry-rohan
final1 = "::".join(list) # sharad::harry::rohan
# print(final1)


# Format methods ( not used much )

# FORMAT METHOD (STRINGS)
# Formats the values inside the string into a desired output.
# template.format(p1,p2...)



sharad = "{} is a good {}".format("sharad", "boy") # sharad is a good boy
# If we want we can also set it like boy is a good sharad ( done below )

reversed_sharad = "{1} is a good {0}".format("sharad", "boy")
print(sharad) # sharad is a good boy
print(reversed_sharad) # boy is a good sharad

