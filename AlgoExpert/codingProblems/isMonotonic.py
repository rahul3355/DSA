def isMonotonic(array):
    # Write your code here.
    monotonic = True
    if len(array) == 0 or len(array) == 1:
        return monotonic
    element1 = array[0]
    element2 = array[1]

    if element1 == element2:
        element1 = array[1]
        element2 = array[2]
        

    if element1 > element2:
        monotonic = checkMonotonicDecreasing(array)
    else:
        monotonic = checkMonotonicIncreasing(array)

    return monotonic

def checkMonotonicDecreasing(array):
    for i in range(len(array)-1):
        left = array[i]
        right = array[i+1]
        if right > left:
            return False
    return True

def checkMonotonicIncreasing(array):
    for i in range(len(array)-1):
        left = array[i]
        right = array[i+1]
        if left > right:
            return False
    return True
            

    
