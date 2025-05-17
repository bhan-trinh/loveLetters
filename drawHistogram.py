import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

NUMBER_OF_WORDS = 20

def graphHistogram():
    words = []
    freq = []
    with open('wordCounter.csv') as wordCounterFile:
        lineNum = 0
        headers = wordCounterFile.readline().split(",")
        for line in wordCounterFile.readlines():
            word, frequency = line.split(",")
            words.append(word)
            freq.append(int(frequency))
            lineNum += 1

            if lineNum > NUMBER_OF_WORDS:
                break

    # Creating bar chart
    plt.bar(words, freq)

    # Adding value labels
    add_labels(words, freq)

    # Adding title and labels
    plt.title("Love Letters Word Frequency")
    plt.xlabel("Words")
    plt.ylabel("Frequency")

    # Display the chart
    plt.show()


# Function to add value labels on top of bars
def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])  # Placing text slightly above the bar

if __name__ == "__main__":
    graphHistogram()