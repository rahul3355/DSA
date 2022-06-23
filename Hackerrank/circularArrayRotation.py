def rotate(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l, r = l+1, r-1

def circularArrayRotation(a, k, queries):
    # Write your code here
    k = k % len(a)
    
    rotate(a, 0, len(a)-1)
    rotate(a, 0, k-1)
    rotate(a, k, len(a)-1)
    
    ls = []
    for query in queries:
        ls.append(a[query])
    
    return ls