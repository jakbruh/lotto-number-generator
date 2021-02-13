from random import sample
from math import ceil, floor

numbersToEnter = []
leftoverNumbersFromEachSet = []



def createPossibleNumbers(availableNumbers):
    return list(range(1, availableNumbers))

def createEntries(winningNumberLength, numberOfGamesBought, numberRangeInDraw):
    possibleNumbers = createPossibleNumbers(numberRangeInDraw + 1)
    entriesToFulfillAllNumbers = ceil(len(possibleNumbers) / winningNumberLength)
    for _ in range(1, entriesToFulfillAllNumbers):
        numberFromPossibleNumbers = sample(possibleNumbers, winningNumberLength)
        for number in numberFromPossibleNumbers:
            possibleNumbers.remove(number)
        print(numberFromPossibleNumbers)
    leftoverNumbersFromEachSet.append(possibleNumbers)

def main():
    winningNumberLength = int(input("How many numbers can you pick in each game? E.g 6 \n"))
    numberOfGamesBought = int(input("How many games did you buy?\n"))
    numberRangeInDraw = int(input("What is the maximum number in the draw? e.g 45\n"))

    setsNeeded = floor(numberOfGamesBought / winningNumberLength)

    for _ in range(1, setsNeeded):
        createEntries(winningNumberLength, numberOfGamesBought, numberRangeInDraw)
    print(leftoverNumbersFromEachSet)

main()
