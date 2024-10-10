def railDecrypt(cipherText, numRails):
    railLen = len(cipherText) // numRails
    solution = ''
    for col in range(railLen):
        for rail in range(numRails):
            nextLetter = col + (rail * railLen)
            solution = solution + cipherText[nextLetter]
    return solution.split()

def createWordDict(dName):
    myDict = {}
    with open(dName, 'r') as myFile:
        for line in myFile:
            myDict[line[:-1]] = True  #set all values to True
    return myDict


def railBreak(cipherText):
    wordDict = createWordDict('wordlist.txt')
    cipherLen = len(cipherText)
    maxGoodSoFar = 0
    bestGuess = "No words found in dictionary" #default response
    for i in range(2, cipherLen + 1):
        words = railDecrypt(cipherText, i)
        goodCount = 0     #reset for new list
        for w in words:
            if w in wordDict:
                goodCount = goodCount + 1
        if goodCount > maxGoodSoFar:   #if more words in this list
            maxGoodSoFar = goodCount
            bestGuess = " ".join(words) #join words in list with space
    return bestGuess
