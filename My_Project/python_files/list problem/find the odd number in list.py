# WAP to find the odd number in list
def odd(arr):
    arr1 = []
    for i in arr:
        if (i%2!=0):
            arr1.append(i)
    return arr1
l1 = [2,3,4,5,6]
print(odd(l1))