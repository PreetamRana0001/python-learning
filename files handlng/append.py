def append_to_file(filename):
    text = input("enter new line: ")
    with open(filename, "a") as f:
        f.write(text + "\r\n")

append_to_file("poem.txt")