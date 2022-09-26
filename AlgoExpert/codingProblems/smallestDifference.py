def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    currDiff, smallDiff = 10000, 10000

    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            currDiff = arrayOne[i] - arrayTwo[j]
            currDiff = abs(currDiff)

            if smallDiff > currDiff:
                element1 = arrayOne[i]
                element2 = arrayTwo[j]
                smallDiff = currDiff

    print(smallDiff)
    return [element1, element2]
