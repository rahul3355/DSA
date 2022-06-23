def extraLongFactorials(n):
    # Write your code here
    mul = 1
    for i in range(n,1,-1):
        mul *= i
    print(mul)