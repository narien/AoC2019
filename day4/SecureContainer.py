import sys

def checkDoubleDigit(value):
    prevChar = 'a'
    currCount = 1
    countOfRecurrance = {1}
    for i in str(value):
        if i == prevChar:
            currCount += 1
        else:
            countOfRecurrance.add(currCount)
            currCount = 1
        prevChar = i
    countOfRecurrance.add(currCount)
    return (len(countOfRecurrance) > 1, 2 in countOfRecurrance)

def isIncreasing(value):
    ints = [int(i) for i in str(value)]
    currInt = 0
    for i in ints:
        if i < currInt:
            return False
        currInt = i
    return True

def countValidPasswords(lowerBound, upperBound):
    partOneCount = 0
    partTwoCount = 0
    current = lowerBound
    while current < upperBound:
        if(isIncreasing(current)):
            doubleOrBigger, exclusiveDouble = checkDoubleDigit(current)
            if doubleOrBigger:
                partOneCount += 1
            if exclusiveDouble:
                partTwoCount += 1
        current += 1

    return (partOneCount, partTwoCount)

if __name__ == '__main__':
    lowerBound = int(sys.argv[1])
    upperBound = int(sys.argv[2])

    partOne, partTwo = countValidPasswords(lowerBound, upperBound)

    print("Part 1: %i" % partOne)
    print("Part 2: %i" % partTwo)
