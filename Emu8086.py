
registers = {'AX': 0, 'BX': 0, 'CX': 0, 'DX': 0, 'SI': 0, 'DI': 0, 'BP': 0, 'SP': 0}
text = {}
blocks = {}
stack = []
eip = 2
equal = False

archiveToRead = 'OrgaProFinal.txt'


def getBlocks():
    archive = open(archiveToRead, 'r')
    i = 1
    for line in archive:
        if ':' in line:
            blocks.update({line.split(':')[0]: i})
        i += 1
    archive.close()


def readArchive():
    archive = open(archiveToRead, 'r')
    i = 1
    for line in archive:
        text.update({i: line.rstrip('\n')})
        i += 1
    archive.close()


def MOV(x):
    o = x.split(',')
    try:
        registers[o[0]] = int(o[1])
    except ValueError:
        registers[o[0]] = int(registers[o[1]])


def INC(x):
    registers[x] = registers.get(x) + 1


def DEC(x):
    registers[x] = registers.get(x) - 1


def ADD(x):
    o = x.split(',')
    try:
        registers[o[0]] = registers.get(o[0]) + int(o[1])
    except ValueError:
        registers[o[0]] = registers.get(o[0]) + registers.get(o[1])


def SUB(x):
    o = x.split(',')
    try:
        registers[o[0]] = registers.get(o[0]) - int(o[1])
    except ValueError:
        registers[o[0]] = registers.get(o[0]) - registers.get(o[1])


def MUL(x):
    try:
        registers['AX'] = registers.get('AX') * int(x)
    except ValueError:
        registers['AX'] = registers.get('AX') * registers.get(x)


def DIV(x):
    try:
        registers['DX'] = registers.get('AX') % x
        registers['AX'] = int(registers.get('AX') / int(x))
    except ZeroDivisionError:
        print('Division by 0 is not possible')
    except TypeError:
        registers['DX'] = registers.get('AX') % registers.get(x)
        registers['AX'] = int(registers.get('AX') / registers.get(x))


def CMP(x):
    global equal
    o = x.split(',')

    equal = registers.get(o[0]) == int(o[1])


def PUSH(x):
    stack.append(registers.get(x))


def POP():
    if 0 < len(stack):
        stack.pop()


def Jump(x):
    global eip
    if x == 'END':
        eip = len(text)
    eip = blocks.get(x) - 1


def printResults():
    print(registers)
    print(stack)


def order(option):
    operation = option[0]
    if operation == 'MOV':
        MOV(option[1])
        printResults()
    if operation == 'ADD':
        ADD(option[1])
        printResults()
    if operation == 'DIV':
        DIV(option[1])
        printResults()
    if operation == 'MUL':
        MUL(option[1])
        printResults()
    if operation == 'SUB':
        SUB(option[1])
        printResults()
    if operation == 'PUSH':
        PUSH(option[1])
        printResults()
    if operation == 'POP':
        POP()
        printResults()
    if operation == 'INC':
        INC(option[1])
        printResults()
    if operation == 'DEC':
        DEC(option[1])
        printResults()
    if operation == 'CMP':
        CMP(option[1])
    if operation == 'JMP':
        Jump(option[1])
    if operation == 'JE' and equal:
        Jump(option[1])
    if operation == 'JNE' and not equal:
        Jump(option[1])


def main():
    global eip
    getBlocks()
    readArchive()
    while eip < len(text):
        line = text[eip]
        if line == '':
            eip += 1
        else:
            if 'RET' in line:
                eip = len(text)
                print('')

            else:
                if ':' in line:
                    command = line.split(':')[1]
                else:
                    command = line
                option = command.split(' ')
                while '' in option:
                    option.remove('')
                if 0 < len(option):
                    order(option)
                eip += 1


main()
