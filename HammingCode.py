import math


def getParity(listMessage, listParity):
    parityLength = int(math.log(len(listMessage)-1, 2)) + 1
    for x in range(parityLength):
        listParity.append(listMessage[-1 - (2 ** x)])
    return parityLength


def calculateParity(listMessage, parityLength, parity):
    listMessage[-1] = 0
    GP = sum(listMessage) % 2
    for x in range(parityLength):
        listMessage[-1 - (2 ** x)] = 0
    counter = 0

    binary = open('HammingCode.csv', 'r', encoding='UTF-8')
    for line in binary:
        counter -= 1

        bit = line.split(',')
        b1 = bit[5]
        b2 = bit[4]
        b3 = bit[3]
        b4 = bit[2]
        b5 = bit[1]
        b6 = bit[0]
        if listMessage[counter] == 1 and b1 == '1\n':
            parity[0] += 1
        if listMessage[counter] == 1 and b2 == '1':
            parity[1] += 1
        if listMessage[counter] == 1 and b3 == '1':
            parity[2] += 1
        if listMessage[counter] == 1 and b4 == '1':
            parity[3] += 1
        if listMessage[counter] == 1 and b5 == '1':
            parity[4] += 1
        if listMessage[counter] == 1 and b6 == '1':
            parity[5] += 1
        if counter == -len(listMessage):
            break
    for y in range(parityLength):
        parity[-y] = parity[-y] % 2
    binary.close()
    return parity, GP


def main():
    message = input()
    listParity = []
    listMessage = list(map(int, str(message)))
    GP = listMessage[-1]
    syndrome = []
    parity = []
    nullParity = []

    parityLength = getParity(listMessage, listParity)

    for x in range(parityLength):
        parity.append(0)
        nullParity.append("0")

    newParity, GPnew = calculateParity(listMessage, parityLength, parity)

    for x in range(parityLength):
        x += 1
        if newParity[-x] != listParity[-x]:
            syndrome.append('1')
        else:
            syndrome.append('0')
    print("")
    if syndrome == nullParity:
        print("No error")
    else:
        if GP == GPnew:
            print("DED")
        else:
            print("SEC")
            print("Syndrome = ", int(''.join(syndrome), 2)
)


main()
