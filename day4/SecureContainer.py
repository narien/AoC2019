import sys

def isIncreasing(value):
    ints = [i for i in str(value)]
    intsSorted = sorted(ints)
    return ints == intsSorted

def validatePassword(value):
    if not isIncreasing(value): return (0, 0)

    digitDict = {i:str(value).count(i) for i in set(str(value))}
    return (1 if len(digitDict) < 6 else 0, 1 if 2 in digitDict.values() else 0)

def countValidPasswords(lowerBound, upperBound):
    partOneCount, partTwoCount = 0, 0
    for i in range(lowerBound, upperBound):
        p1, p2 = validatePassword(i)
        partOneCount += p1
        partTwoCount += p2
    return (partOneCount, partTwoCount)

if __name__ == '__main__':
    lowerBound = int(sys.argv[1])
    upperBound = int(sys.argv[2])

    partOne, partTwo = countValidPasswords(lowerBound, upperBound)

    print("Part 1: %i" % partOne)
    print("Part 2: %i" % partTwo)
