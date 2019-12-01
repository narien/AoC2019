def recursiveFuelCost(fuel):
    extraFuel = (fuel // 3) - 2
    return 0 if extraFuel <= 0 else extraFuel + recursiveFuelCost(extraFuel)

def CalculateFuelCost(moduleArr):
    moduleTotal = 0
    additionalFuelTotal = 0
    for mass in moduleArr:
        moduleFuel = (mass // 3) - 2
        moduleTotal += moduleFuel
        additionalFuelTotal += recursiveFuelCost(moduleFuel)
    return moduleTotal, additionalFuelTotal

if __name__ == '__main__':
    moduleArr = []
    with open('input.txt') as f:
        for line in f:
            moduleArr.append(int(line))
    moduleTotal, additionalFuel = CalculateFuelCost(moduleArr)        
    print('part 1: ' + str(moduleTotal))
    print('part 2: ' + str(moduleTotal + additionalFuel))