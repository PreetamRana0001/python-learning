# write a program to find out whether a given post is talking about "preetam" 
POST = input("ENTER A POST:")
if "Preetam".lower() in POST.lower():
    print("preetam word is present ")
else:
    print("preetam word is not present")
