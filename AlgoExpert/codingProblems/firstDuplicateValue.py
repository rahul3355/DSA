def firstDuplicateValue(array):
    # Write your code here.
    hashNumbers = {}

    for i in range(len(array)):
        number = array[i]
        hashNumbers[number] = True

        if i == len(array)-1:
            return -1 
            
        nextNumber = array[i+1]

        if nextNumber in hashNumbers:
            return nextNumber

    return -1
