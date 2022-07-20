def isValidSubsequence(array, sequence):
    # O(n) Time | O(1) Space
    arrIdx = 0
    sqnIdx = 0

    while arrIdx < len(array) and sqnIdx < len(sequence):
        if array[arrIdx] == sequence[sqnIdx]:
            sqnIdx += 1
        arrIdx += 1

    if sqnIdx == len(sequence):
        return True
    else:
        return False