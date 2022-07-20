def twoNumberSum(array, targetSum):

    # O(nlog(n)) Time | O(1) Space

    # 1. Sort the array
    array.sort()
    # 2. Initialize left and right pointers
    left = 0
    right = len(array) - 1
    # 3. Calculate currSum by adding left and right
    while left < right:
        currSum = array[left] + array[right]
        # 4. Check currSum == target
        if currSum == targetSum:
            return [array[left], array[right]]
        else: 
            # 5. if currSum > target: decrement right
            if currSum > targetSum:
                right -= 1
            # 6. if currSum < target: increment left
            else:
                left += 1

    return []