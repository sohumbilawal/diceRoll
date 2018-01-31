from random import *
import heapq

d1 = 0
d2 = 0
d3 = 0

#i = 0

numADice = 3
numDDice = 2

aDice = []

def diceRoll(num):
    i = 0
    while (i < num):
        die = randint(1,6)
        aDice.extend([die])
        i += 1
    #aDice.extend([max(aDice)])
    return aDice

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
    print("Rolling 3 dice: ", diceRoll(3))
elif numADice == 2:
    print("Rolling 2 dice: ", diceRoll(2))
elif numADice == 1:
    print("Rolling 1 die: ", diceRoll(1))

#aHeap = heapq.heapify(aDice)
highA = heapq.nlargest(2, aDice[0:len(aDice)])
maxA = highA[0]
max2A = highA[1]
print("The highest attacker roll is: {0}, and second highest is: {1}".format(maxA, max2A))
#print(aDice)

#print(aDice)
#print(d1, d2, d3)
#print("MAX: " , max(aDice))
