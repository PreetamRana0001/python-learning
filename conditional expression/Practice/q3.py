'''A spam comment is defines as a text containg following keywords:
"make a lot of money", "buy now", "subscribe this", "click this", "visit this"
.write a program to detect these spam comments.'''
comment = input("enter a comment")
if(comment == "make a lot of money" or comment == "buy now" or comment == "subscribe this" or comment == "click this" or comment == "visit this"):
     print("this is a spam comment")
else:
   print("good comment")