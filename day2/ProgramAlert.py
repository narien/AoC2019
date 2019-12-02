def runProgram(program):
    instructionPointer = 0
    while program[instructionPointer] == 1 or program[instructionPointer] == 2 or program[instructionPointer] == 99:
        if program[instructionPointer] == 1:
            program[program[instructionPointer + 3]] = program[program[instructionPointer + 1]] + program[program[instructionPointer + 2]]
        elif program[instructionPointer] == 2:
            program[program[instructionPointer + 3]] = program[program[instructionPointer + 1]] * program[program[instructionPointer + 2]]
        elif program[instructionPointer] == 99:
            return program[0]
        instructionPointer += 4

if __name__ == '__main__':
    program = []
    with open('input.txt') as f:
        for line in f:
            program += ([int(i) for i in line.split(',') if i.strip().isdigit()])


    for i in range(100):
        for j in range(100):
            currProgram = program.copy()
            currProgram[1] = i
            currProgram[2] = j
            res = runProgram(currProgram)
            if i == 12 and j == 2:
                print("Part 1: " + str(res))
            if currProgram[0] == 19690720:
                print("Part 2: " + str(100 * i + j))
