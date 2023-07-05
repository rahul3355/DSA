def arrayOfProducts(array):
    # Write your code here.
    productArray = []
    productLeft, productRight = 1,1
    
    for i in range(len(array)):
        productLeft = findProductLeft(array, i)
        productRight = findProductRight(array, i)

        finalProduct = productLeft * productRight

        productArray.append(finalProduct)

    return productArray

def findProductLeft(array, index):
    productLeft = 1
    if index == 0:
        return 1
    if index == 1:
        return array[0]
    for i in range(index-1, -1, -1):
        productLeft = productLeft * array[i]

    return productLeft

def findProductRight(array, index):
    productRight = 1
    if index == len(array)-1:
        return 1
    if index == len(array)-2:
        return array[len(array)-1]
    for i in range(index+1, len(array)):
        productRight = productRight * array[i]

    return productRight