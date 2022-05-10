# WAP to swap the first and last element of a list.

def swap(arr):
     start,*middle,last = arr
     arr = [last,*middle,start]
     return arr

newlist = [4,7,9,12]
print(swap(newlist))






