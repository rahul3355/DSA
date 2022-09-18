def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    # O(nlog(n)) time | O(1) space
    sumTotal = 0
    if fastest:
        redShirtSpeeds.sort(reverse=True)
    else:
        redShirtSpeeds.sort()
        
    blueShirtSpeeds.sort()
    sumTotal = 0
    for i in range(len(redShirtSpeeds)):
        if redShirtSpeeds[i] > blueShirtSpeeds[i]:
            sumTotal += redShirtSpeeds[i]
        else:
            sumTotal += blueShirtSpeeds[i]
    return sumTotal