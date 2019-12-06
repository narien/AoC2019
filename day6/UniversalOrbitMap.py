def countTotalOrbits(orbits):
    totalOrbits = 0
    for key in orbits:
        tempKey = key
        currOrbits = 0
        while True:
            if tempKey in orbits:
                currOrbits += 1
                tempKey = orbits[tempKey]
            else:
                totalOrbits += currOrbits
                break
    return totalOrbits

def getOrbitSet(val, orbits):
    orbitSet = set()
    while True:
        if val in orbits:
            val = orbits[val]
            orbitSet.add(val)
        else:
            # print(orbitList)
            return orbitSet

def countOrbitsBetween(start, finish, orbits):
    startSet = getOrbitSet(start, orbits)
    finishSet = getOrbitSet(finish, orbits)

    startDiff = startSet - finishSet
    finishDiff = finishSet - startSet
    return len(startDiff) + len(finishDiff)

if __name__ == '__main__':
    with open('input.txt') as f:
        orbits = dict(orb.strip().split(')')[::-1] for orb in f.readlines())

        # print(orbits)
        print("Part 1: %i" % countTotalOrbits(orbits))
        print("Part 2: %i" % countOrbitsBetween("YOU", "SAN", orbits))