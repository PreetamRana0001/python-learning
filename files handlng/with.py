f = open("file.txt")

print(f.read())
f.close

# the same

with open("file.txt") as f:
    print(f.read)