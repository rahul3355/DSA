def classPhotos(redShirtHeights, blueShirtHeights):
    # O(nlog(n)) time | O(1) space
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[0] > blueShirtHeights[0]:
        classPhotoPossible = compareShirtHeights(redShirtHeights, blueShirtHeights)
    else:
        classPhotoPossible = compareShirtHeights(blueShirtHeights, redShirtHeights)

    return classPhotoPossible

def compareShirtHeights(largerArray, smallerArray):
    for idx in range(len(largerArray)):
        if smallerArray[idx] >= largerArray[idx]:
            return False
    return True