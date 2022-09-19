def generateDocument(characters, document):
    # Write your code here.
    for character in document:
        countCharFreq = countChar(character, characters)
        countDocFreq = countChar(character, document)
        if countDocFreq > countCharFreq:
            return False
    return True



def countChar(character, target):
    count = 0
    for char in target:
        if char == character:
            count += 1
    return count