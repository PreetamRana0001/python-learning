with open("poem.txt") as f:
    st = f.read()
    if "Twinkle" in st:
         print("present")
    else:
            print("no")
