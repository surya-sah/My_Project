#  Write a program to display all prime numbers within a range
start = 2
stop = 8
for x in range (start,stop+1):
    if x>1:
        for num in range (2,x):
            if x % num == 0:
                break
        else:
            print (x)