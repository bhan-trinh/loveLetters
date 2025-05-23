import kagglehub
from collections import Counter
import os
import re
import csv

POS_TAGS = ["NN", "VB", "JJ"]

def main():
    # Download latest version
    path = kagglehub.dataset_download("fillerink/love-letters")
    posDict = loadPosTags('words_pos.csv')

    letterNumber = 1
    wordCounter = Counter()

    while True:
        try:
            letterFileName = os.path.join(path, f"{letterNumber}.txt")
            letterFile = open(letterFileName, encoding="utf8")
        except FileNotFoundError:
            break
        letterCounter = parseLetter(letterFile, posDict)
        wordCounter += letterCounter
        

        print(f"================{letterNumber}==================")
        
        '''        for word in letterCounter:
            print(f"{word} : {letterCounter[word]}")
        '''
        for pair in letterCounter.most_common(5):
            if pair[1] != 1:
                print(f"{pair[0]}: {pair[1]}")
        
        letterNumber += 1

    print(f"================Summary==================")

    '''
    for key in wordCounter.most_common(20):
        if wordCounter[key] != 1:
            print(f"{key} : {wordCounter[key]}")
    '''

    for pair in wordCounter.most_common(20):
        if pair[1] != 1:
            print(f"{pair[0]}: {pair[1]}")

    writeFreqCSV(wordCounter)

def parseLetter(letterFile, posDict):
    letterCounter = Counter()

    for line in letterFile.readlines():
        words = wordTokenize(line)
        for word in words:
            word = word.lower()
            if word in posDict and word != "ha":
                if posDict[word] in POS_TAGS:
                    letterCounter[word] += 1
    return letterCounter 
    

def loadPreposition(prepFileName):
    # Prepositions
    with open(prepFileName) as prepFile:
        prepositions = []
        for line in prepFile.readlines():
            if "#" not in line: 
                line = line.replace("\n", "")
                prepositions.append(line)
        return prepositions


def loadPosTags(csvFileName):
    with open(csvFileName) as csvFile:
        csvDict = csv.DictReader(csvFile)
        posDict = {}
        for wordEntry in csvDict:
            word = wordEntry["word"]
            posTag = wordEntry["pos_tag"]
            posDict[word] = posTag
        return posDict


def wordTokenize(string):
    replacements = str.maketrans({
        "’": "",
        "'": "",
        ".": "",
        "!": "",
        "?": "",
        })
    words = string.translate(replacements)
    words = words.split()
    return words


def writeFreqCSV(wordCounter : Counter):
    with open('wordCounter.csv', 'w', newline='') as csvfile:
        fieldnames = ['word', 'frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for word in wordCounter.most_common():
            writer.writerow({'word': word[0], 'frequency': word[1]})


if __name__ == "__main__":
    main()