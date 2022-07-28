def isValidSubsequence(array, sequence):
    
    # O(n) time | O(1) space
    arrIdx = 0
    sqnIdx = 0

    while arrIdx < len(array) and sqnIdx < len(sequence):
        if array[arrIdx] == sequence[sqnIdx]:
            sqnIdx += 1
        arrIdx += 1
    
    return sqnIdx == len(sequence)