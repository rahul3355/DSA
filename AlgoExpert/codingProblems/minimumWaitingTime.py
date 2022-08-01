from array import array


def minimumWaitingTime(queries):
    # Write your code here.

    # O(nlog(n)) time | O(1) space

    if len(queries) == 0:
        return 0
    
    queries.sort()

    sumTotal = 0
    grandSum = 0

    for i in range(0,len(queries)-1):
        sumTotal += queries[i]
        grandSum += sumTotal

    return grandSum

# Algorithm:
# 1. Sort the array
# 2. Loop through array and keep track of currentSum and add it to grandSum after each iteration