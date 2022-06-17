def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    maxPurchase = min(keyboards) + min(drives)
    if maxPurchase > b:
        return -1
    for keyboard in keyboards:
        for drive in drives:
            x = keyboard + drive
            if x > maxPurchase and x <= b:
                maxPurchase = x
    
    return maxPurchase
    