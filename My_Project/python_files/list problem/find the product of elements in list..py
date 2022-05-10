# WAP to find the product of elements in list.
def product(arr):
    total_product = 1
    for i in arr:
        total_product=total_product*i
    return total_product
l1 = [2,3,4]
print(product(l1))

