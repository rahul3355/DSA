def moveElementToEnd(array, toMove):
    # Write your code here.
    array.sort()
    res = []
    [res.append(x) for x in array if x != toMove]
    countMove = array.count(toMove)
    for j in range(countMove):
        res.append(toMove)
    print(res)
    return res
