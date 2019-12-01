def calcCost(weight):
    return (weight // 3) - 2

def recursiveFuelCost(fuel):
    extraFuel = calcCost(fuel)
    return 0 if extraFuel <= 0 else extraFuel + recursiveFuelCost(extraFuel)

def CalculateFuelCost(moduleArr):
    modulesTotal = 0
    additionalFuelTotal = 0
    for mass in moduleArr:
        moduleFuel = calcCost(mass)
        modulesTotal += moduleFuel
        additionalFuelTotal += recursiveFuelCost(moduleFuel)
    return modulesTotal, additionalFuelTotal

if __name__ == '__main__':
    moduleArr = []
    with open('input.txt') as f:
        for line in f:
            moduleArr.append(int(line))
    modulesTotal, additionalFuel = CalculateFuelCost(moduleArr)        
    print('part 1: ' + str(modulesTotal))
    print('part 2: ' + str(modulesTotal + additionalFuel))