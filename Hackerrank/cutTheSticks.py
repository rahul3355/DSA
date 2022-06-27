def cutTheSticks(arr):
    # Write your code here
    newArr = []
    newArr.append(len(arr))
    while True:
        arr = [i for i in arr if i!=min(arr)]
        if len(arr)==0:
            break
        newArr.append(len(arr))
        
    return newArr