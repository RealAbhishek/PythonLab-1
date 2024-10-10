from removematches import *

def readFile(fileName):
    with open(fileName, 'r', encoding='utf-8') as wells:
	    return wells.read()


def letterFrequency(text):
    text = text.lower()
    nonLetters = removeMatches(text, 'abcdefghijklmnopqrstuvwxyz')
    text = removeMatches(text, nonLetters)
    lCount = {}
    total = len(text)
    for ch in text:    #count each letter�s occurrence
        lCount[ch] = lCount.get(ch, 0) + 1
    for ch in lCount:  #calculate percentages
        lCount[ch] = lCount[ch] / total
    return lCount

def getFreq(t):
    return t[1]    #return second item in the tuple

def maybeAdd(ch, toList):
    if ch in 'abcdefghijklmnopqrstuvwxyz' and ch not in toList:
	    toList.append(ch)

def neighborCount(text):
    nbDict = {}
    text = text.lower()
    for i in range(len(text) - 1):
        nbList = nbDict.setdefault(text[i], [])
        maybeAdd(text[i + 1], nbList)
        nbList = nbDict.setdefault(text[i + 1], [])
        maybeAdd(text[i], nbList)
    for key in nbDict.keys():
        nbDict[key] = len(nbDict.get(key))
    return nbDict

