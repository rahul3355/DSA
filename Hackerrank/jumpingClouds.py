def jumpingOnClouds(c, k):
    energy=100
    pos=0
    n=len(c)
    while True:
        pos=(pos+k)%n
        if c[pos]==1:
            energy-=3
        else:
            energy-=1
        
        if pos==0:
            break
    return energy
                   