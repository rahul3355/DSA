# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, level=1):
    # O(n) time | O(d) space, where d is the greatest depth of special array
    sumTotal = 0
    for element in array:
        if type(element) is list:
            sumTotal += productSum(element, level+1)
        else:
            sumTotal += element
    return sumTotal * level