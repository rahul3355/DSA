def addThese(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + addThese(arr[1:])


arr = [25,24,1,50]
print(addThese(arr))