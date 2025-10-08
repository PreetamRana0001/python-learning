# problem 1
name = input("enter you name:")
print(f"Good afternoon {name}") # f string 


# problem 2
letter = '''Dear <|NAME|>,
You are selected! 
Date: <|DATE|>'''

print(letter.replace("<|NAME|>" ,"preetam rana").replace("<|DATE|>" , "10/01/2001"))

# problem 3 detect double space in a string
name =  " preetam rana is a good  boy"
print(name.find("  "))

# problem 4 replace double space in a string
name =  " preetam rana is a good boy"
print(name.replace("  "," "))

# problem 5
letter = "Dear preetam rana, \n\t this python course is nice. \nThanks!"
print(letter)
