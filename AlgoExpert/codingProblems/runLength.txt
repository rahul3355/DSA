def runLengthEncoding(string):
    currRun = 1
    encoded = []

    for i in range(1, len(string)):
        currChar = string[i]
        prevChar = string[i-1]

        if currChar != prevChar or currRun == 9:
            encoded.append(str(currRun))
            encoded.append(prevChar)
            currRun = 0
            
        currRun += 1

    encoded.append(str(currRun))
    encoded.append(string[len(string)-1])

    return "".join(encoded)