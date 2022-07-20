def sortedSquaredArray(array):
    # Write your code here.

    # O(nlog(n)) Time | O(1) Space
    for i in range(len(array)):
        x = array[i] * array[i]
        array[i] = x
    array.sort()
    return array
