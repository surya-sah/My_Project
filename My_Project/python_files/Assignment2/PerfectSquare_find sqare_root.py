''' Write a python script to check whether an entered number
is a perfect square or not if yes find its square root '''

num = int(input("enter any number"))
under_root= num**0.5
if under_root**2==num :
    print("perfect square")
    print("square root = ", num**2)
else:
    print("not perfect square")