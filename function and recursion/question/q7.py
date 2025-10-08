def rem(l,word):
    n = []
    for item in l:
       if not(item == word):
           n.append(item.strip(word))
    return n
l = ["preetam", "soni","sonuan","an"]
print(rem(l,"an"))
