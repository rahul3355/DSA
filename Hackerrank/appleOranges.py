def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apl_distance = []
    for i in apples:
        x = a + i
        if s <= x and t >= x:
            apl_distance.append(x)
        
    or_distance = []
    for j in oranges:
        y = b + j
        if s <= y and t >= y:
            or_distance.append(y)
    
    print(len(apl_distance))
    print(len(or_distance))