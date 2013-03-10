#!/usr/bin/python

import random

doors = {}
doors['prize'] = 1

def choose():
    doors['chosen'] = random.randint(1, 3)

def isWinner():
    return doors['chosen'] == doors['prize']

def openDoor():
    possible = range(1,4)
    available = lambda x : x not in (doors['chosen'], doors['prize'])
    doors['open'] = random.choice(filter(available, possible))

def switch():
    possible = range(1,4)
    available = lambda x : x not in (doors['chosen'], doors['open'])
    doors['chosen'] = random.choice(filter(available, possible))

def playSwitch():
    choose()
    openDoor()
    switch()

def playStick():
    choose()
    openDoor()


if __name__ == '__main__':

    rounds = 10000
    winSwitch = 0 
    winStick = 0   
    for i in range(rounds):
        playSwitch()
        if isWinner():
            winSwitch += 1
        playStick()
        if isWinner():
            winStick += 1 
    print "Won %d of %d (%.02f%%) when switching doors" % (winSwitch, rounds, 100.0 * winSwitch / rounds)
    print "Won %d of %d (%.02f%%) when not switching doors" % (winStick, rounds, 100.0 * winStick / rounds)
