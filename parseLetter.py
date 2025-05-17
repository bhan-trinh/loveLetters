import matplotlib.pyplot as plt
import numpy as np
import kagglehub
from collections import Counter
import os
import re
import csv

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

def parseLetter(letterFile, posDict):
    letterCounter = Counter()

    for line in letterFile.readlines():
        words = wordTokenize(line)
        for word in words:
            word = word.lower()
            if word in posDict and word != "ha":
                if posDict[word] in ["NN", "VB", "JJ"]:
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


def graphHistogram():
    # Generate data
    data = np.random.randn(1000)

    # Plot a histogram
    plt.hist(data, bins=30, color='skyblue', edgecolor='black')

    # Add labels and title
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Basic Histogram')

    plt.show()


if __name__ == "__main__":
    main()