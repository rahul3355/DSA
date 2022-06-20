def pickingNumbers(a):
    # Write your code here
    a.sort()
    setarr = set(a)
    listarr = list(setarr)
    print(listarr)
    if len(listarr) == 1:
        return a.count(listarr[0])
    maxCount, newCount = 1,1
    for i in range(len(listarr) - 1):
        if listarr[i] == listarr[i+1] or listarr[i] == listarr[i+1] - 1:
            x = a.count(listarr[i])
            y = a.count(listarr[i+1])
            if x+y > maxCount:
                maxCount = x + y
        if a.count(listarr[i]) > maxCount:
            maxCount = a.count(listarr[i])
    return maxCount