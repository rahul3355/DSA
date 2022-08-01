def classPhotos(redShirtHeights, blueShirtHeights):
    
    # o(nlog(n)) time | O(1) space

    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[0] > blueShirtHeights[0]:
        bool = compareShirtHeight(redShirtHeights, blueShirtHeights)
    else:
        bool = compareShirtHeight(blueShirtHeights, redShirtHeights)
    
    return bool

def compareShirtHeight(largerArray, smallerArray):
    for idx in range(len(largerArray)):
        if largerArray[idx] <= smallerArray[idx]:
            return False
    return True
