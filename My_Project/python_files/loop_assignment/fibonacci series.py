#  Display Fibonacci series up to 10 terms
num1 = 0
num2 = 1
counter = 10
for x in range (0,counter):
    print (num1, end=' ')
    result = num1+num2
    num1 = num2
    num2 = result


