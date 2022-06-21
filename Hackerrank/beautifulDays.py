def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    for x in range(i,j+1):
        x = str(x)
        rev_x = x[::-1]
        rev_x = int(rev_x)
        x = int(x)
        
        if abs(x-rev_x) % k == 0:
            count += 1
    
    return count