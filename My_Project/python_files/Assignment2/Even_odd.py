''' Write a python script to check whether a number is odd or even,
if it is odd convert it to even and vice versa.'''

num = int(input(" Enter any number"))
if num % 2 == 0:
    print("number is even")
    print(num + 1)
else:
    print("number is odd")
    print(num + 1)