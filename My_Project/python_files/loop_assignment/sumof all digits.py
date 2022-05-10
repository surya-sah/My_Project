# sum all the digit in a given number
x = 3456
sum = 0
digit = 0
while (x != 0):

    digit = x % 10
    sum = sum + digit
    x = x//10

print(sum)