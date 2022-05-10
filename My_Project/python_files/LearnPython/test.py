'''def check(arr):
    if len(arr) <= 1:
        return arr
    else:
        left_arr = []
        right_arr = []
        for item in arr:
            if item == 0:
                left_arr.append(item)
            else:
                right_arr.append(item)
        return (left_arr)+(right_arr)

print(check([0,1,0,0,0,1,1,0]))'''

def graph(arr):
    res=0
    for i in range (1,len(arr)-1):
        left = arr[i]
        for j in range(i):
            left = max(left,arr[j])
        right = arr[i]
        for j in range (i+1,len(arr)):
            right= max(right,arr[j])

        res= res+(min(left,right)-arr[i])
    return res
l1 = [4,1,7,2,1,6]
print(graph(l1))