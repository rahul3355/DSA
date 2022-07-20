def isValidSubsequence(array, sequence):
    # Write your code here.

    # O(n) Time | O(1) Space
    sqnIdx = 0
    for element in array:
        if sqnIdx == len(sequence):
            break
        if sequence[sqnIdx] == element:
            sqnIdx += 1

    return sqnIdx == len(sequence)
