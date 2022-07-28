def nonConstructibleChange(coins):
    coins.sort()
    minimumChange = 0

    for coin in coins:
        if coin > minimumChange + 1:
            return minimumChange + 1
        minimumChange += coin
    return minimumChange+1