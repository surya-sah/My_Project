# Find the factorial of a given number
num = int(input("enter any number"))
result = 1
for x in range (num,0,-1):
    result = result * x
else:
    print(result)