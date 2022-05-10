def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

        item_greater = []
        item_lower = []
        for item in arr:
            if item < pivot:
                item_lower.append(item)
            else:
                item_greater.append(item)
        return quick_sort(item_lower)+[pivot]+quick_sort(item_greater)
print(quick_sort([3,6,2,8,4,9]))