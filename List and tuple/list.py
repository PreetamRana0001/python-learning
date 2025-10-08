friends = ["apple" , "orange" , "banana"] # list is mutable
print(type(friends))
print(friends[0])
friends.append("grapes")
print(friends)
friends.remove("orange")
print(friends)
friends[1]= "kiwi"
print(friends)