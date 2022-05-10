# Take input of age of 3 people by user and determine oldest and youngest among them

p1 = int(input("write first person age."))
p2 = int(input("write second person age."))
p3 = int(input("write third person age."))
if (p1 > p2) and (p1 > p3):
    print("older people : ", p1)
elif (p2 > p1) and (p2 > p3):
    print("older people : ", p2)
else:
    print("older people : ", p3)
if (p1 < p2) and (p1 < p3):
    print("younger people : ", p1)
elif (p2 < p1) and (p2 < p3):
    print("younger people : ", p2)
else:
    print("younger people : ", p3)