def firstNonRepeatingCharacter(string):
    # Write your code here.
    stringArr = [x for x in string]
    for i in range(0, len(stringArr)):
        freqChar = countFreq(string[i], stringArr)
        if freqChar == 1:
            return i
    return -1

def countFreq(char, target):
    count = 0
    for c in target:
        if c == char:
            count += 1
    print(count)
    return count