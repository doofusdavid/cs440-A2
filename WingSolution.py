
import math
import numpy

def squarable(state):
    import math
    sqrt = math.sqrt(len(state))

    if sqrt % 1 != 0:
        print( "Not a Squareable List")
        return False
    else:
        return True


def printState_8p(state):
    '''
    Displays the current state of a list by squaring it, and displaying it nicely.
    :param state: list of numbers
    :return: displays list as a square
    '''
    if type(state) is not list:
        print("Not a valid list")
    
    # Substitute '' for 0, to make the puzzle look better
    display = [x if x !=0 else '' for x in state]
    sqrt = squareOfState(state)

    # Iterate through the list, display tab-delimited
    for x in range(sqrt):
        print(*display[( x *sqrt):( x *sqrt) + sqrt], sep='\t')


def findBlank_8p(state):

    index = state.index(0)
    sqrt = squareOfState(state)

    position =  index % sqrt, int(index / sqrt)
    return position

def actionsF_8p_generator(state):

    position = findBlank_8p(state)
    sqrt = int(math.sqrt(len(state)))

    if position[0] != 0 : yield "left"
    if position[0] != sqrt- 1: yield "right"
    if position[1] != 0: yield "up"
    if position[1] != sqrt - 1: yield "down"

def actionsF_8p(state):
    import math
    
    position = findBlank_8p(state)
    sqrt = int(math.sqrt(len(state)))

    actions = []
    if position[0] != 0 : actions.append("left")
    if position[0] != sqrt- 1: actions.append("right")
    if position[1] != 0: actions.append("up")
    if position[1] != sqrt - 1: actions.append("down")
    return actions


def squareOfState(state):
    import math
    if not squarable(state):
        return "State not squarable"

    return int(math.sqrt(len(state)))


def goalTest(state, testState):
    return state == testState


def legalAction(arrState, action, position, sqrt):
    if action == "left" and position[0] == 0:
        return False
    if action == "right" and position[0] == sqrt - 1:
        return False
    if action == "up" and position[1] == 0:
        return False
    if action == "down" and position[1] == sqrt - 1:
        return False

    return True


def takeActionF_8p(state, action):
    import numpy
    
    position = findBlank_8p(state)
    sqrt = squareOfState(state)

    arrState = numpy.reshape(state, (sqrt, sqrt))
    if not legalAction(arrState, action, position, sqrt):
        return "Could not move that direction"

    if action == "left": return swap(arrState, position, (position[0] - 1, position[1]))
    if action == "right": return swap(arrState, position, (position[0] + 1, position[1]))
    if action == "up": return swap(arrState, position, (position[0], position[1] - 1))
    if action == "down": return swap(arrState, position, (position[0], position[1] + 1))


def swap(state, location1, location2):
    state[location1[1]][location1[0]], state[location2[1]][location2[0]] = state[location2[1]][location2[0]], \
                                                                           state[location1[1]][location1[0]]
    return list(state.flat)

def depthLimitedSearch(startState, actionsF, takeActionF, goalState, depthLimit):
    if goalState == startState:
        return []

    if depthLimit == 0:
        return 'cutoff'
    else:
        cutoffOccurred = False

    for action in actionsF(startState):
        #print("Action: " + action)
        childState = takeActionF(startState, action)
        #printState(childState)

        result = depthLimitedSearch(childState, actionsF, takeActionF, goalState, depthLimit-1)

        if result is 'cutoff':
            cutoffOccurred = True
        elif result is not 'failure':
            result.append(childState)
            return result

    if cutoffOccurred:
        return 'cutoff'
    else:
        return 'failure'


def iterativeDeepeningSearch(startState, goalState, actionsF, takeActionF, maxDepth):

    solutionPath = []
    solutionPath.append(startState)
    #if set(startState) != set(goalState):
        ##if set(startState) != set(goalState) or not solvablePuzzle(startState):
        #return "No solution possible"

    for depth in range(maxDepth):
        print("depth: " + str(depth))
        result = depthLimitedSearch(startState, actionsF, takeActionF, goalState, depth)

        if result is 'failure':
            return 'failure'
        if result is not 'cutoff':
            # for oneresult in result:
            #     solutionPath.append(oneresult)
            # return solutionPath
            result.append(startState)
            #result.sort(reverse=True)
            return result

    return 'cutoff'

def countInversions(startState):
    inversions = 0
    for state in startState:
        for predecessors in startState[startState.index(state):]:
            if state > predecessors:
                inversions += 1

    return inversions


def solvablePuzzle(startState):
    if countInversions(startState) % 2 == 0:
        return True
    else:
        return False


def printPath_8p(solutionPath):
    for result in solutionPath:
        printState_8p(result)
        print()

import random
def randomStartState(goalState, actionsF, takeActionF, nSteps):
    state = goalState
    for i in range(nSteps):
        state = takeActionF(state, random.choice(actionsF(state)))
    return state

goalState = [1, 2, 3, 4, 0, 5, 6, 7, 8]

#startState = randomStartState(goalState, actionsF_8p, takeActionF_8p, 10)
#print(startState)

#startState = [1, 3, 2, 4, 7, 5, 6,8, 0]
goalState = [1, 2, 3, 4, 0, 5, 6, 7, 8]
startState = [1, 0, 3, 4, 2, 5, 6, 7, 8]
startState = [1, 5, 2, 4, 7, 3, 0, 6, 8]
#startState = [4, 7, 2, 1, 6, 5, 0, 3, 8]
#solutionPath = iterativeDeepeningSearch(startState, goalState, actionsF_8p, takeActionF_8p, 15)
#printPath_8p(solutionPath)
# Delete all variables defined so far (in notebook)
for name in dir():
    if not callable(globals()[name]) and not name.startswith('_'):
        del globals()[name]

import numpy as np
import os
import copy

# import A2mysolution as mine
# iterativeDeepeningSearch = mine.iterativeDeepeningSearch
# depthLimitedSearch = mine.depthLimitedSearch
# findBlank_8p = mine.findBlank_8p
# actionsF_8p = mine.actionsF_8p
# takeActionF_8p = mine.takeActionF_8p
# printPath_8p = mine.printPath_8p

# def within(correct, attempt, diff):
#     return np.abs((correct-attempt) / correct)  < diff

g = 0

for func in ['iterativeDeepeningSearch', 'depthLimitedSearch',
             'findBlank_8p', 'actionsF_8p', 'takeActionF_8p', 'printPath_8p']:
    if func not in dir() or not callable(globals()[func]):
        print('CRITICAL ERROR: Function named \'{}\' is not defined'.format(func))
        print('  Check the spelling and capitalization of the function name.')


succs = {'a': ['b', 'z', 'd'], 'b':['a'], 'e':['z'], 'd':['y'], 'y':['z']}
print('\nSearching this graph:\n', succs)
def aF(state):
    return copy.copy(succs.get(state,[]))
def tAF(state, action):
    return action
print('\nLooking for path from a to y with max depth of 1.')
path = iterativeDeepeningSearch('a', 'y', aF, tAF, 1)
if type(path) == str and path.lower() == 'cutoff':
    g += 5
    print(' 5/ 5 points. Your search correctly returned', path)
else:
    print(' 0/ 5 points. Your search should have returned ''cutoff''. You returned', path)

print('\nLooking for path from a to y with max depth of 5.')
path = iterativeDeepeningSearch('a', 'z', aF, tAF, 5)
if path == ['a', 'z']:
    g += 10
    print('10/10 points. Your search correctly returned', path)
else:
    print(' 0/10 points. Your search should have returned', ['a', 'z'])


print('\nTesting findBlank_8p([1, 2, 3, 4, 5, 6, 7, 0, 8])')
r, c = findBlank_8p([1, 2, 3, 4, 5, 6, 7, 0, 8])
if r == 2 and c == 1:
    g += 5
    print(' 5/ 5 points. Your findBlank_8p correctly returned', r, c)
else:
    print(' 0/ 5 points. Your findBlank_8p should have returned 2 1 but you returned', r, c)

print('\nTesting actionsF_8p([1, 2, 3, 4, 5, 6, 7, 0, 8])')
acts = actionsF_8p([1, 2, 3, 4, 5, 6, 7, 0, 8])
correct = ['left', 'right', 'up']
if acts == correct:
    g += 10
    print('10/10 points. Your actionsF_8p correctly returned', acts)
else:
    print(' 0/10 points. Your actionsF_8p should have returned', correct, 'but you returned', acts)

print('\nTesting takeActionF_8p([1, 2, 3, 4, 5, 6, 7, 0, 8],''up'')')
s = takeActionF_8p([1, 2, 3, 4, 5, 6, 7, 0, 8],'up')
correct = [1, 2, 3, 4, 0, 6, 7, 5, 8]
if s == correct:
    g += 10
    print('10/10 points. Your takeActionsF_8p correctly returned', s)
else:
    print(' 0/10 points. Your takeActionsF_8p should have returned', correct, 'but you returned', s)


print('\nTesting iterativeDeepeningSearch([1, 2, 3, 4, 5, 6, 7, 0, 8],[0, 2, 3, 1, 4,  6, 7, 5, 8], actionsF_8p, takeActionF_8p, 5)')
path = iterativeDeepeningSearch([1, 2, 3, 4, 5, 6, 7, 0, 8],[0, 2, 3, 1, 4,  6, 7, 5, 8], actionsF_8p, takeActionF_8p, 5)
correct = [[1, 2, 3, 4, 5, 6, 7, 0, 8], [1, 2, 3, 4, 0, 6, 7, 5, 8], [1, 2, 3, 0, 4, 6, 7, 5, 8], [0, 2, 3, 1, 4, 6, 7, 5, 8]]
if path == correct:
    g += 20
    print('20/20 points. Your search correctly returned', path)
else:
    print(' 0/20 points. Your search should have returned', correct, 'but you returned', path)

print('\nTesting iterativeDeepeningSearch([5, 2, 8, 0, 1, 4, 3, 7, 6], [0, 2, 3, 1, 4,  6, 7, 5, 8], actionsF_8p, takeActionF_8p, 10)')
path = iterativeDeepeningSearch([5, 2, 8, 0, 1, 4, 3, 7, 6],[0, 2, 3, 1, 4,  6, 7, 5, 8], actionsF_8p, takeActionF_8p, 10)
if type(path) == str and path.lower() == 'cutoff':
    g += 20
    print('20/20 points. Your search correctly returned', path)
else:
    print(' 0/20 points. Your search should have returned ''cutoff'', but you returned', path)


print('\n{} Grade is {}/80'.format(os.getcwd().split('/')[-1], g))
print('Up to 20 more points will be given based on the qualty of your descriptions of the method and the results.')


