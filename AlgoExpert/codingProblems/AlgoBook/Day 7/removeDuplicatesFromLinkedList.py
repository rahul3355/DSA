# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # O(n) time | O(1) space
    currentNode = linkedList
    while currentNode is not None:
        nextDistinct = currentNode.next
        while nextDistinct is not None and currentNode.value == nextDistinct.value:
            nextDistinct = nextDistinct.next
        currentNode.next = nextDistinct
        currentNode = nextDistinct
    return linkedList
