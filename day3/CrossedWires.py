import sys

def manhattanDist(x, y):
    return abs(x) + abs(y)

def takeStep(direction, x, y, stepsTaken):
    stepsTaken += 1
    if direction == 'U':
        y += 1
    elif direction == 'R':
        x += 1
    elif direction == 'D':
        y -= 1
    elif direction == 'L':
        x -= 1
    return x, y, stepsTaken

def mapLine(line):
    lineCoords = {}
    x, y = 0, 0
    stepsTaken = 0
    for move in line:
        newSteps = int(move[1:])
        for _ in range(newSteps):
            x, y, stepsTaken = takeStep(move[0], x, y, stepsTaken)
            lineCoords[(x, y)] = (manhattanDist(x, y), stepsTaken)
    return lineCoords

def findClosestOverlapDistance(firstLine, newLine):
    closestDistToOrigin = sys.maxsize
    shortestWalk = sys.maxsize
    x, y = 0, 0
    stepsTaken = 0
    for move in newLine:
        newSteps = int(move[1:])
        for _ in range(newSteps):
            x, y, stepsTaken = takeStep(move[0], x, y, stepsTaken)
            if (x, y) in firstLine:
                currDist = firstLine[(x, y)][0]
                if currDist < closestDistToOrigin:
                    closestDistToOrigin = currDist
                if stepsTaken + firstLine[(x, y)][1] < shortestWalk:
                    shortestWalk = stepsTaken + firstLine[(x, y)][1]
    return closestDistToOrigin, shortestWalk

if __name__ == '__main__':
    with open('input.txt') as f:
        lineOne = [x.strip() for x in f.readline().split(',')]
        lineTwo = [x.strip() for x in f.readline().split(',')]

    firstLine = mapLine(lineOne)
    manhattanDist, walkingDist = findClosestOverlapDistance(firstLine, lineTwo)
    print("Part 1: " + str(manhattanDist))
    print("Part 2: " + str(walkingDist))
