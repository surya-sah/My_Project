# Calculate the cube of all numbers from 1 to a given number
num = int(input("enter any number"))
x = 1
while x<=num:
    cube = x**3
    print("current number is :",x ,"and the cube is :",cube)
    x += 1