import os

# directory ka path do
path = "C:/Users"   # <-- yahan apna directory path likho

# check karo directory exist karti hai ya nahi
if os.path.exists(path):
    print(f"Contents of directory: {path}\n")
    for item in os.listdir(path):
        print(item)
else:
    print("Directory not found!")
