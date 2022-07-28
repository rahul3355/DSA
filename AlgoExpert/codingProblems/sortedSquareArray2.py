def sortedSquaredArray(array):
    minValue = 0
    maxValue = len(array) - 1
    newArr = [0 for x in range(len(array))]
    ptr = len(array) - 1
    while ptr != -1:
        if abs(array[minValue]) > abs(array[maxValue]):
            value = array[minValue]
            newArr[ptr] = value * value
            minValue += 1
            ptr -= 1
        else:
            value = array[maxValue]
            newArr[ptr] = value * value
            maxValue -= 1
            ptr -= 1
    return newArr
            
            