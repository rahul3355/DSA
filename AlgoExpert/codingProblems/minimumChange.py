def nonConstructibleChange(coins):

    # O(nlog(n)) time | O(1) space

    coins.sort()

    minimumChange = 0
    
    for coin in coins:
        if coin > minimumChange + 1:
            break
        minimumChange += coin
    return minimumChange + 1