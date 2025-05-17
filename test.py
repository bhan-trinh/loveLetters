# Test separate letters for cleaning

import kagglehub
from collections import Counter
import os
from nltk.stem import WordNetLemmatizer
from parseLetter import loadPosTags, wordTokenize


LETTERNUM = 2

def main():
    path = kagglehub.dataset_download("fillerink/love-letters")
    posDict = loadPosTags('words_pos.csv')

    letterNumber = LETTERNUM
    wordCounter = Counter()

    try:
        letterFileName = os.path.join(path, f"{letterNumber}.txt")
        letterFile = open(letterFileName, encoding="utf8")
    except FileNotFoundError:
        pass
    letterCounter = parseLetter(letterFile, posDict)
    wordCounter += letterCounter
    

    print(f"================{letterNumber}==================")
    
    for word in letterCounter:
        print(f"{word} : {letterCounter[word]}")
    
    letterNumber += 1


def parseLetter(letterFile, posDict):
    lemmatizer = WordNetLemmatizer()
    letterCounter = Counter()

    for line in letterFile.readlines():
        words = wordTokenize(line)
        for word in words:
            word = word.lower()
            key = word
            if key in posDict and key != "ha":
                if posDict[key] in ["NN", "VB", "JJ"]:
                    letterCounter[key] += 1
                    print(key)
    return letterCounter 

main()