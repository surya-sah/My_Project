# Find the sum of the series upto n terms
# 2+22+222+2222+22222
n = 5
num = 2
sum = 0
for x in range(n):
    print(num, end="+")
    sum = sum + num
    num = num*10+2
print("\n sum is =",sum)
