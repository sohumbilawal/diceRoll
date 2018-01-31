from random import *
import heapq

d1 = 0
d2 = 0
d3 = 0

#i = 0

numADice = 3
numDDice = 2

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

if numADice == 3:
    print("Rolling 3 dice: ", diceRollA(3))

    highA = heapq.nlargest(2, aDice[0:len(aDice)])
    maxA = highA[0]
    max2A = highA[1]
    print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))

elif numADice == 2:
    print("Rolling 2 dice: ", diceRollA(2))

    highA = heapq.nlargest(2, aDice[0:len(aDice)])
    maxA = highA[0]
    max2A = highA[1]
    print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))

elif numADice == 1:
    print("Rolling 1 die: ", diceRollA(1))

    maxA = max(aDice)
    print("The highest attacker roll is: {0}".format(maxA))

if numDDice == 2:
    print("Rolling 2 dice: ", diceRollD(2))

    highD = heapq.nlargest(2, dDice[0:len(dDice)])
    maxD = highD[0]
    max2D = highD[1]
    print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxD, max2D))

elif numDDice == 1:
    print("Rolling 1 die: ", diceRollD(1))

    maxD = max(dDice)
    print("The highest attacker roll is: {0}".format(maxD))

#aHeap = heapq.heapify(aDice)
#highA = heapq.nlargest(2, aDice[0:len(aDice)])
#maxA = highA[0]
#max2A = highA[1]
#print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))
#print(aDice)

#print(aDice)
#print(d1, d2, d3)
#print("MAX: " , max(aDice))
