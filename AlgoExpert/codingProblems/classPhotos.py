def classPhotos(redShirtHeights, blueShirtHeights):
    # O(nlog(n)) time | O(n) space
    redShirtHeights.sort()
    blueShirtHeights.sort()


    largerArray, smallerArray = compareArray(redShirtHeights, blueShirtHeights)
    for idx in range(len(largerArray)):
        if largerArray[idx] <= smallerArray[idx]:
            return False
    return True


def compareArray(redShirtHeights, blueShirtHeights):
    if blueShirtHeights[0] > redShirtHeights[0]:
        largerArray = blueShirtHeights
        smallerArray = redShirtHeights
    else:
        largerArray = redShirtHeights
        smallerArray = blueShirtHeights
    return largerArray, smallerArray

# Algorithm:
# 1. sort the arrays.
# 2. assign largerArray and smallerArray by comparing.
# 3. Loop through largerArray (or smallerArray), compare elements