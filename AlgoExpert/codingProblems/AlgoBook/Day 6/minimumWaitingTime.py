def minimumWaitingTime(queries):
    # O(nlog(n)) time | O(1) space
    currentSum = 0
    grandSum = 0
    queries.sort()

    for i in range(len(queries)-1):
        currentSum += queries[i]
        grandSum += currentSum

    return grandSum