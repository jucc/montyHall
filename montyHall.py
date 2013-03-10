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

if __name__ == '__main__':
    choose()
    peek()
    
