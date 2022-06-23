def findDigits(n):
    # Write your code here
    strNum = str(n)
    strNumList = list(strNum)
    #strNumListSet = set(strNumList)

    count = 0
    for digit in strNumList:
        x = int(digit)
        if x == 0:
            continue
        elif n % x == 0:
            count += 1
    return count