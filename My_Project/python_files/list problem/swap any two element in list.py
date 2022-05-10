# WAP to swap any two elements of a list.
def swap(arr,pos1,pos2):
    arr[pos1],arr[pos2]=arr[pos2],arr[pos1]
    return arr
list1 = [75,98,65,90]
p1=2
p2=3
print(swap(list1,p1,p2))
