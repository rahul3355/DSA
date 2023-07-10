def minHeightBst(array):
    return constructMinHeightBST(array, 0, len(array)-1)


def constructMinHeightBST(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
    bst.left = constructMinHeightBST(array, startIdx, midIdx - 1)
    bst.right = constructMinHeightBST(array, midIdx+1, endIdx)
    return bst