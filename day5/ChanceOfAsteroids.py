def opCode(val):
    l = [0] * 5
    i = -1
    for c in reversed(str(val)):
        l[i] = int(c)
        i -= 1
    return l

def getVal(i, mode, program):
    if mode == 0:
        return program[program[i]]
    else:
        return program[i]

def runProgram(program, input):
    iP = 0
    while True:
        op = opCode(program[iP])
        if op[4] == 1:
            program[program[iP+3]] = getVal(iP+1, op[2], program) + getVal(iP+2, op[1], program)
            iP += 4
        elif op[4] == 2:
            program[program[iP+3]] = getVal(iP+1, op[2], program) * getVal(iP+2, op[1], program)
            iP += 4
        elif op[4] == 3:
            program[program[iP+1]] = input
            iP += 2
        elif op[4] == 4:
            print("opcode 4 print: %i" % getVal(iP+1, op[2], program))
            iP += 2
        elif op[4] == 5:
            if not getVal(iP+1, op[2], program) == 0:
                iP =  getVal(iP+2, op[1], program)
            else:
                iP += 3
        elif op[4] == 6:
            if getVal(iP+1, op[2], program) == 0:
                iP =  getVal(iP+2, op[1], program)
            else:
                iP += 3
        elif op[4] == 7:
            program[program[iP+3]] = 1 if getVal(iP+1, op[2], program) < getVal(iP+2, op[1], program) else 0
            iP += 4
        elif op[4] == 8:
            program[program[iP+3]] = 1 if getVal(iP+1, op[2], program) == getVal(iP+2, op[1], program) else 0
            iP += 4
        elif op[3]*10 + op[4] == 99:
            print("Program done.")
            return program[0]

if __name__ == '__main__':
    program = []
    with open('input.txt') as f:
        program += ([int(i) for i in f.readline().split(',')])

    print("Part 1:")
    runProgram(program.copy(), 1)
    print("Part 2:")
    runProgram(program.copy(), 5)
