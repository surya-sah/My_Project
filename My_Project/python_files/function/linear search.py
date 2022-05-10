def check(l1, num):
    found = False

    for i in l1:
        if i == num:
            found = True
    return found


test = [3, 5, 6, 78, 43]
print(check(test, 5))
