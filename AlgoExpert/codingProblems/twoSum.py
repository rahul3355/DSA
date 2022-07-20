def twoNumberSum(array, targetSum):
    # Write your code here.

    # 1. Add numbers to hashtable.
    # 2. Looped through given array and checked if x = targetSum - array[i] is present in hashtable.
    # 3. Checked condition x != array[i]
    # 4. return [x, array[i]] if found, [] if not.

    # O(n) time | O(n) Space
    hashArr = {}
    for i in range(len(array)):
        hashArr[i] = array[i]

    for i in range(len(array)):
        x = targetSum - array[i]
        if x in hashArr.values() and x != array[i]:
            return [x,array[i]]
    return []
