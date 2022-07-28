def validateSubsequence(array, sequence):
    arrIdx = 0
    sqnIdx = 0

    # O(n) time | O(1) space
    while arrIdx < len(array) and sqnIdx < len(sequence):
        if array[arrIdx] == sequence[sqnIdx]:
            sqnIdx += 1
        arrIdx += 1
    return sqnIdx == len(sequence)