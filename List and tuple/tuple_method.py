a = ("preetam rana", "30 june 2001") # tuple is immutable
for i in a:
    print(i)
print(type(a))

no = a.count(45) # it counts the number of occurrences of 45 in the tuple

print(no)
print(len(a)) # it gives the length of the tuple