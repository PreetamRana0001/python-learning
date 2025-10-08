d = {} # empty dictionary
print(type(d))
mark =  { 
    "sonu": 100,
    "preetam": 90,
    "soni": 80
}
print(mark.items())
print(mark.keys())
print(mark.values())
mark.update({"sonu":99})
mark.update({"sonika":"fail"})
print(mark)
print(mark.get("sonu")) # it will give value if key is present
print(mark.get("sonu1")) # it will give none if key is not present
print(mark["preetam1"])  # it will give error if key is not present