def equalizeArray(arr):
    # Write your code here
    mostOccured = 1
    for element in arr:
        x = arr.count(element)
        if x > mostOccured:
            mostOccured = x
    
    return len(arr) - mostOccured