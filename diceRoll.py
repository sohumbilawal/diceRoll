from random import *
import heapq
import time

d1 = 0
d2 = 0
d3 = 0

#i = 0

aTroops = int(input('How many troops are attacking: '))
dTroops = int(input('How many troops are defending: '))

delay = int(input('How long would you like to wait between rolls (in seconds): '))
#numADice = 3
#numDDice = 2

aDice = []
dDice = []

def diceRollA(num):
    i = 0
    while (i < num):
        die = randint(1,6)
        aDice.extend([die])
        i += 1
    #aDice.extend([max(aDice)])
    return aDice

def diceRollD(num):
    i = 0
    while (i < num):
        die = randint(1,6)
        dDice.extend([die])
        i += 1
    #aDice.extend([max(aDice)])
    return dDice

#aDice = [d1, d2, d3]

#for die in aDice:
#    die = randint(1,6)
#    aDice[i] = die
#    i +=1
#x = randint(1,6)

#d1 = aDice[0]
#d2 = aDice[1]
#d3 = aDice[2]
while aTroops >= 0 or dTroops >= 0:

#    if aTroops > 3:
#        numADice = 3
#    elif aTroops <= 3:
#        numADice = aTroops
#    print(numADice, aTroops)

#    if dTroops > 2:
#        numDDice = 2
#    elif dTroops <= 2:
#        numDDice = dTroops
#    print(numDDice, dTroops)

    if aTroops >= 3 and dTroops >= 2:
        aDice = []
        dDice = []

        print("Rolling 3 attacking dice: ", diceRollA(3))
        print("Rolling 2 defending dice: ", diceRollD(2))

        highA = heapq.nlargest(2, aDice[0:len(aDice)])
        maxA = highA[0]
        max2A = highA[1]
        print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))

        highD = heapq.nlargest(2, dDice[0:len(dDice)])
        maxD = highD[0]
        max2D = highD[1]
        print("The highest defender roll is: {0}, and second highest is: {1}".format(maxD, max2D))

        if maxD >= maxA and max2D >= max2A:
            aTroops = aTroops - 2
        elif maxD >= maxA and max2D < max2A:
            aTroops = aTroops - 1
            dTroops = dTroops - 1
        elif maxD < maxA and max2D >= max2A:
            dTroops = dTroops - 1
            aTroops = aTroops - 1
        elif maxD < maxA and max2D < max2A:
            dTroops = dTroops - 2

        print (aTroops, dTroops)

    elif aTroops >= 3 and dTroops == 1:
        aDice = []
        dDice = []

        print("Rolling 3 attacking dice: ", diceRollA(3))
        print("Rolling 1 defending dice: ", diceRollD(1))

        highA = heapq.nlargest(2, aDice[0:len(aDice)])
        maxA = highA[0]
        max2A = highA[1]
        print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))

        maxD = max(dDice)
        print("The highest defender roll is: {0}".format(maxD))

        if maxD >= maxA:
            aTroops = aTroops - 1
        elif maxD < maxA:
            dTroops = dTroops - 1

        print (aTroops, dTroops)

    elif aTroops == 2 and dTroops == 2:
        aDice = []
        dDice = []

        print("Rolling 2 attacking dice: ", diceRollA(2))
        print("Rolling 2 defending dice: ", diceRollD(2))

        highA = heapq.nlargest(2, aDice[0:len(aDice)])
        maxA = highA[0]
        max2A = highA[1]
        print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))

        highD = heapq.nlargest(2, dDice[0:len(dDice)])
        maxD = highD[0]
        max2D = highD[1]
        print("The highest defender roll is: {0}, and second highest is: {1}".format(maxD, max2D))

        if maxD >= maxA and max2D >= max2A:
            aTroops = aTroops - 2
        elif maxD >= maxA and max2D < max2A:
            aTroops = aTroops - 1
            dTroops = dTroops - 1
        elif maxD < maxA and max2D >= max2A:
            dTroops = dTroops - 1
            aTroops = aTroops - 1
        elif maxD < maxA and max2D < max2A:
            dTroops = dTroops - 2

        print (aTroops, dTroops)

    elif aTroops == 2 and dTroops == 1:
        aDice = []
        dDice = []

        print("Rolling 2 attacking dice: ", diceRollA(2))
        print("Rolling 1 defending dice: ", diceRollD(1))

        highA = heapq.nlargest(2, aDice[0:len(aDice)])
        maxA = highA[0]
        max2A = highA[1]
        print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))

        maxD = max(dDice)
        print("The highest defender roll is: {0}".format(maxD))

        if maxD >= maxA:
            aTroops = aTroops - 1
        elif maxD < maxA:
            dTroops = dTroops - 1

        print (aTroops, dTroops)

    elif aTroops == 1 and dTroops == 2:
        aDice = []
        dDice = []

        print("Rolling 1 attacking die: ", diceRollA(1))
        print("Rolling 2 defending dice: ", diceRollD(2))

        maxA = max(aDice)
        print("The highest attacker roll is: {0}".format(maxA))

        highD = heapq.nlargest(2, dDice[0:len(dDice)])
        maxD = highD[0]
        max2D = highD[1]
        print("The highest defender roll is: {0}, and second highest is: {1}".format(maxD, max2D))

        if maxD >= maxA:
            aTroops = aTroops - 1
        elif maxD < maxA:
            dTroops = dTroops - 1

        print (aTroops, dTroops)

    elif aTroops == 1 and dTroops == 1:
        aDice = []
        dDice = []

        print("Rolling 1 attacking die: ", diceRollA(1))
        print("Rolling 1 defending dice: ", diceRollD(1))

        maxA = max(aDice)
        print("The highest attacker roll is: {0}".format(maxA))

        maxD = max(dDice)
        print("The highest defender roll is: {0}".format(maxD))

        if maxD >= maxA:
            aTroops = aTroops - 1
        elif maxD < maxA:
            dTroops = dTroops - 1

        print (aTroops, dTroops)

    else:
        break

    time.sleep(delay)
    
if aTroops > dTroops:
    print("Attacking army wins! Troops left: {0}".format(aTroops))
elif dTroops > aTroops:
    print("Defending army wins! Troops left: {0}".format(dTroops))
#aHeap = heapq.heapify(aDice)
#highA = heapq.nlargest(2, aDice[0:len(aDice)])
#maxA = highA[0]
#max2A = highA[1]
#print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))
#print(aDice)

#print(aDice)
#print(d1, d2, d3)
#print("MAX: " , max(aDice))
