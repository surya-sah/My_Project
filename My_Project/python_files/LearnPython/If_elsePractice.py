name = input("Enter your name? ")
if len(name) < 3:
    print("name must be at least 3 character")
elif len(name) > 50:
    print("name can be maximum 50 character")
else:
    print("name looks good!")
