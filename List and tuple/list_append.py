friends = ["apple" , "orange" , "banana"]
print(type(friends)) # printing the type of friends
print(friends[0])
friends.append("grapes")  # appending grapes to the list
print(friends)
friends.remove("orange") # removing orange from the list
print(friends)
friends[1]= "kiwi"
print(friends)

l1 = [234,542,332,5,235,5,23,55,55]
l1.sort() # for sorting the list
l1.reverse() # for reversing the list
l1.insert(2, 100) # for inserting an element at index 2
print(l1) # printing the list

l1.pop(6) # for deleting an element at index 6
print(l1)
l1.remove(234) # for removing the first occurrence of 5
print(l1)   