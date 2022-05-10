# WAP to count the occurrence of element in list.
def check (arr,n):
    count = 0
    for i in arr:
        if (i == n):
            count+=1
    return count
l1 = [2,5,4,2,6,2,7,2,9,2]
k = 2
print(check(l1,k))