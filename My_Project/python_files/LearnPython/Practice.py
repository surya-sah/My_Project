'''def binary_search(arr,n):
    left_index=0
    right_index=len(arr)
    mid_index=0

    while left_index<=right_index:
        mid_index=(left_index+right_index)//2
        mid_number=arr[mid_index]
        if mid_number==n:
            return True
        elif mid_number<n:
            left_index=mid_index+1
        else:
            right_index=mid_index-1
    return False


l1 = [5,6,7,8,9]
m = 7
if binary_search(l1,m):
     print("found")
else:
    print("notfound")'''
'''
def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        print(j)
        while j >0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1

list = [2,6,4,9,7,8]
insertion_sort(list)
print(list)'''

def selection_sort(arr):
    for i in range(len(arr)-1):
        current_min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[current_min_index]:
                current_min_index=j
        arr[i],arr[current_min_index]=arr[current_min_index],arr[i]


list = [2, 6, 4, 9, 7, 8]
selection_sort(list)
print(list)