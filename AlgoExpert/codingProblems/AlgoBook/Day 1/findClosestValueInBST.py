def findClosestValueInBst(tree, target):
    # O(log(N)) time | O(1) space
    currentNode = tree
    minDifference = abs(target - currentNode.value)

    while currentNode is not None:
        if target < currentNode.value:
            newDifference = abs(target - currentNode.value)
            if newDifference < minDifference:
                minDifference = newDifference
                temp = currentNode.value
            currentNode = currentNode.left
        elif target > currentNode.value:
            newDifference = abs(target - currentNode.value)
            if newDifference < minDifference:
                minDifference = newDifference
                temp = currentNode.value
            currentNode = currentNode.right
        else:
            return currentNode.value
    return temp