


import math
import numpy

def squarable(state):
    sqrt = math.sqrt(len(state))

    if sqrt % 1 != 0:
        print( "Not a Squareable List")
        return False
    else:
        return True


def printState(state):
    '''
    Displays the current state of a list by squaring it, and displaying it nicely.
    :param state: list of numbers
    :return: displays list as a square
    '''

    sqrt = squareOfState(state)

    # Iterate through the list, display tab-delimited
    for x in range(sqrt):
        print(*state[(x*sqrt):(x*sqrt) + sqrt], sep='\t')


def findBlank(state):

    index = state.index(0)
    sqrt = squareOfState(state)

    print(index)
    position =  index % sqrt, int(index / sqrt)
    return position

def actionsF(state):

    position = findBlank(state)
    sqrt = int(math.sqrt(len(state)))

    if position[0] != 0 : yield "left"
    if position[0] != sqrt-1 : yield "right"
    if position[1] != 0 : yield "up"
    if position[1] != sqrt-1 : yield "down"

def squareOfState(state):
    if not squarable(state):
        return "State not squarable"

    return int(math.sqrt(len(state)))


def legalAction(arrState, action, position, sqrt):

    if action == "left" and position[0] == 0:
        return False
    if action == "right" and position[0] == sqrt-1:
        return False
    if action == "up" and position[1] == 0:
        return False
    if action == "down" and position[1] == sqrt-1:
        return False

    return True

def takeActionF(state, action):
    position = findBlank(state)
    sqrt = squareOfState(state)

    arrState = numpy.reshape(state, (sqrt,sqrt))
    if not legalAction(arrState, action, position, sqrt):
        return "Could not move that direction"

    if action == "left": return swap(arrState, position, (position[0]-1, position[1]))
    if action == "right": return swap(arrState, position, (position[0]+1, position[1]))
    if action == "up": return swap(arrState, position, (position[0], position[1]-1))
    if action == "down": return swap(arrState, position, (position[0], position[1]+1))

def swap(state,location1, location2):
    state[location1[1]][location1[0]], state[location2[1]][location2[0]] = state[location2[1]][location2[0]], state[location1[1]][location1[0]]
    return list(state.flat)


startState = [1, 2, 3, 4, 2, 5, 0, 7, 8]
printState(startState)
startState = takeActionF(startState, "right")
printState(startState)
startState = takeActionF(startState, "right")
printState(startState)
startState = takeActionF(startState, "right")
print(startState)
#printState(takeActionF(startState, "right"))

for i in actionsF(startState):
    print(i)
