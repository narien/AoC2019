import sys

def manhattanDist(x, y):
    return abs(x) + abs(y)


def mapLine(line):
    lineCoords = {}
    x, y = 0, 0
    stepsTaken = 0
    for move in line:
        if move[0] == 'U':
            yD = int(move[1:])
            for i in range(yD):
                stepsTaken += 1
                y += 1
                lineCoords[(x, y)] = (manhattanDist(x, y), stepsTaken)
        elif move[0] == 'R':
            xD = int(move[1:])
            for i in range(xD):
                stepsTaken += 1
                x += 1
                lineCoords[(x, y)] = (manhattanDist(x, y), stepsTaken)
        elif move[0] == 'D':
            yD = int(move[1:])
            for i in range(yD):
                stepsTaken += 1
                y -= 1
                lineCoords[(x, y)] = (manhattanDist(x, y), stepsTaken)
        elif move[0] == 'L':
            xD = int(move[1:])
            for i in range(xD):
                stepsTaken += 1
                x -= 1
                lineCoords[(x, y)] = (manhattanDist(x, y), stepsTaken)
    return lineCoords

def findClosestOverlapDistance(firstLine, newLine):
    closestDistToOrigin = sys.maxsize
    closestTotalWalkingDist = sys.maxsize
    x, y = 0, 0
    stepsTaken = 0
    for move in newLine:
        if move[0] == 'U':
            yD = int(move[1:])
            for i in range(yD):
                stepsTaken += 1
                y += 1
                if (x, y) in firstLine:
                    currDist = firstLine[(x, y)][0]
                    if currDist < closestDistToOrigin:
                        closestDistToOrigin = currDist
                    if stepsTaken + firstLine[(x, y)][1] < closestTotalWalkingDist:
                        closestTotalWalkingDist = stepsTaken + firstLine[(x, y)][1]

        elif move[0] == 'R':
            xD = int(move[1:])
            for i in range(xD):
                stepsTaken += 1
                x += 1
                if (x, y) in firstLine:
                    currDist = firstLine[(x, y)][0]
                    if currDist < closestDistToOrigin:
                        closestDistToOrigin = currDist
                    if stepsTaken + firstLine[(x, y)][1] < closestTotalWalkingDist:
                        closestTotalWalkingDist = stepsTaken + firstLine[(x, y)][1]
        elif move[0] == 'D':
            yD = int(move[1:])
            for i in range(yD):
                stepsTaken += 1
                y -= 1
                if (x, y) in firstLine:
                    currDist = firstLine[(x, y)][0]
                    if currDist < closestDistToOrigin:
                        closestDistToOrigin = currDist
                    if stepsTaken + firstLine[(x, y)][1] < closestTotalWalkingDist:
                        closestTotalWalkingDist = stepsTaken + firstLine[(x, y)][1]
        elif move[0] == 'L':
            xD = int(move[1:])
            for i in range(xD):
                stepsTaken += 1
                x -= 1
                if (x, y) in firstLine:
                    currDist = firstLine[(x, y)][0]
                    if currDist < closestDistToOrigin:
                        closestDistToOrigin = currDist
                    if stepsTaken + firstLine[(x, y)][1] < closestTotalWalkingDist:
                        closestTotalWalkingDist = stepsTaken + firstLine[(x, y)][1]
    return closestDistToOrigin, closestTotalWalkingDist

if __name__ == '__main__':
    with open('input.txt') as f:
        lineOne = [x.strip() for x in f.readline().split(',')]
        lineTwo = [x.strip() for x in f.readline().split(',')]

    firstLine = mapLine(lineOne)
    manhattanDist, walkingDist = findClosestOverlapDistance(firstLine, lineTwo)
    print("Part 1: " + str(manhattanDist))
    print("Part 2: " + str(walkingDist))
