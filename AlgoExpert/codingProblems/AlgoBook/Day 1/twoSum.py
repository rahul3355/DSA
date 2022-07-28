def twoSum(array, target):
    # O(n) time | O(n) space
    hashMap = {}
    for number in array:
        potentialMatch = target - number
        if potentialMatch in hashMap  and potentialMatch != number:
            return [potentialMatch, number]
        else:
            hashMap[number] = True
    return []