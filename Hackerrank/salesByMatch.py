def sockMerchant(n, ar):
    # Write your code here
    pair = 0
    set_arr = set(ar)
    for sock in set_arr:
        x = ar.count(sock)
        y = x // 2
        pair += y
        
    return pair