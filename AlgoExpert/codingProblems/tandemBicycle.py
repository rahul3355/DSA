def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    # O(nlog(n)) time | O(n) space
    sumTotal = 0
    if fastest:
        sumTotal = fastTandem(redShirtSpeeds, blueShirtSpeeds, len(redShirtSpeeds))
    else:
        sumTotal = slowTandem(redShirtSpeeds, blueShirtSpeeds, len(redShirtSpeeds))
    return sumTotal

def fastTandem(redShirtSpeeds, blueShirtSpeeds, lengthTandem):
    # O(nlog(n)) time | O(n) space
    bigArray = redShirtSpeeds + blueShirtSpeeds
    bigArray.sort(reverse=True)
    sumTotal = 0
    for i in range(lengthTandem):
        sumTotal += bigArray[i]
    return sumTotal

    
def slowTandem(redShirtSpeeds, blueShirtSpeeds, lengthTandem):
    # O(nlog(n)) time | O(1) space
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    sumTotal = 0
    for i in range(lengthTandem):
        if redShirtSpeeds[i] > blueShirtSpeeds[i]:
            sumTotal += redShirtSpeeds[i]
        else:
            sumTotal += blueShirtSpeeds[i]
    return sumTotal
