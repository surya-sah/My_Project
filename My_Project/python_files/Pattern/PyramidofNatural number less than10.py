#1
#234
#56789
counter = 1
for i in range(1,7,2):
    for j in range(i):
        print(counter,end="")
        counter+=1

    print("\n")