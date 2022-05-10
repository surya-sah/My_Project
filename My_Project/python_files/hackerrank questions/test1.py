list1 = [85, 25, 65, 21, 84]
for num in list1:
    x = num % 10
    print(x,end="")
print("\n")
if x % 10 == 0:
    print("number is divisible by 10")
else:
    print("not divisible by 10")

