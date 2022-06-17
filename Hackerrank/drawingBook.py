def pageCount(n, p):
    # Write your code here
    firstpage = 0
    for i in range(n, p, -2):
        if n-1 == p and n%2 == 0:
            firstpage += 1
        elif i <= p or i-1<=p:
            break
        else:
            firstpage += 1
            
    lastpage = 0
    for i in range(1, n, 2):
        if i >= p:
            break
        else:
            lastpage += 1
    

    actualCount = min(firstpage, lastpage)
    return actualCount