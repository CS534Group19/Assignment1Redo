# Author: Oliver Shulman
# Updated: 2/9/2023
# Refactoring: Cutter Beck

import csv
import sys
import time
import random
import math

def main(arg_board_csv, arg_run_time):

    # Read file and create starting board
    startingboard = []

    with open(arg_board_csv, 'r', encoding='utf-8-sig') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            startingboard = startingboard + row

    #Sort strings into integers for sorting

    for i in range(0, len(startingboard)) :
        if startingboard[i] != 'B':
            startingboard[i] = int(startingboard[i])

    #Create 2 possible goal states
    frontboard = list(startingboard)
    backboard = list(startingboard)

    #Replace blank spaces with arbitary integer to go in the front or back of puzzle depending on win state
    for j, item in enumerate(frontboard):
        if item == 'B':
            frontboard[j] = 0

    for q, item in enumerate(backboard):
        if item == 'B':
            backboard[q] = 1000

    #Sort boards to match their win state

    frontboard.sort()
    backboard.sort()

    #Pick Win State and Continuously calculate distance
    if getFrontManhattanDistance(startingboard, frontboard) > getBackManhattanDistance(startingboard, backboard):
        winState = backboard
    else:
        winState = frontboard
   
    print("Initial Manhattan Distance")
    print (CalculateDistance(startingboard, backboard, frontboard, winState))
    
    tic = time.perf_counter()
    data = solution_SimulatedAnnealing(startingboard, backboard, frontboard, winState, arg_run_time)
    toc = time.perf_counter()
    print(data[0])
    print(f"\nSearch took {toc - tic:0.4f} seconds")
    return data


#Calculate Weighted Manhattan Distance for each win state
def getFrontManhattanDistance(anyboard, frontboard):
    totaldistance = 0
    for i in range(len(anyboard)):
        sideLength = math.sqrt(len(anyboard))
        if (anyboard[i] != 0 and anyboard[i] != 1000 and anyboard[i] != 'B'):
            index = frontboard.index(anyboard[i]) + 1            
            
            boardx = (i+1)%sideLength
            winx = index%sideLength
            if boardx == 0:
                boardx = sideLength
            if winx == 0:
                winx = sideLength

            xdistance = abs(boardx - winx)
            ydistance = abs((i+1) - boardx - index + winx) / sideLength

            totaldistance += (xdistance + ydistance)
            
    return totaldistance

def getBackManhattanDistance(anyboard, backboard):
    totaldistance = 0
    for i in range(len(anyboard)):
        sideLength = math.sqrt(len(anyboard))
        if (anyboard[i] != 0 and anyboard[i] != 1000 and anyboard[i] != 'B'):
            index = backboard.index(anyboard[i]) + 1

            boardx = (i+1)%sideLength
            winx = index%sideLength

            if boardx == 0:
                boardx = sideLength
            if winx == 0:
                winx = sideLength

            xdistance = abs(boardx - winx)
            ydistance = abs((i+1) - boardx - index + winx) / sideLength

            totaldistance += (xdistance + ydistance)
    return totaldistance


def CalculateDistance(board, backboard, frontboard, winState):
    if winState == backboard:
        return getBackManhattanDistance(board, backboard)
    else:
        return getFrontManhattanDistance(board, frontboard)

def randomize(blank):
    boardloc = list(blank)
    random.shuffle(boardloc)
    return iter(boardloc)

#Hill Climbing Alg with Simulated Annealing
def hillClimbing(anyBoard, backboard, frontboard, winState, temp):

    #Set Temperature for Annealing

    #Blank Spaces
    for i in randomize(range(len(anyBoard))):
        if anyBoard[i] == 1000 or anyBoard[i] == 0 or anyBoard[i] == 'B':
            break

    d = 0
    d = CalculateDistance(anyBoard, backboard, frontboard, winState)
    if (temp < 0.3):
        temp = 0.3

    sideLength = math.sqrt(len(anyBoard))
    sideLength = int(sideLength)
    while True:
        randCase = random.randint(1,5)
        if randCase == 1:
            if (i >= sideLength and isinstance((anyBoard[i-sideLength]), int)):
                upMove = anyBoard
                upMove[i] = anyBoard[i-sideLength]
                val = upMove[i]
                direction = 'Up'
                upMove[i-sideLength] = 'B'
                if (CalculateDistance(upMove, backboard, frontboard, winState) < d):
                    return upMove, val, direction
                else:
                    deltaE = CalculateDistance(upMove, backboard, frontboard, winState) - d
                    acceptProbability = min(math.exp(deltaE / temp), 1)
                    if random.random() <= acceptProbability:
                        return upMove, val, direction
        elif randCase == 2:
            if (i < (sideLength * sideLength - sideLength) and isinstance((anyBoard[i+sideLength]), int)):
                downMove = anyBoard
                downMove[i] = anyBoard[i+sideLength]
                val = downMove[i]
                direction = 'Down'
                downMove[i+sideLength] = 'B'
                if CalculateDistance(downMove, backboard, frontboard, winState) < d:
                    return downMove, val, direction
                else:
                    deltaE = CalculateDistance(downMove, backboard, frontboard, winState) - d
                    acceptProbability = min(math.exp(deltaE / temp), 1)
                    if random.random() <= acceptProbability:
                        return downMove, val, direction
        elif randCase == 3:
            if (i%sideLength != 0 and isinstance((anyBoard[i-1]), int)):
                leftMove = anyBoard
                leftMove[i] = anyBoard[i-1]
                val = leftMove[i]
                direction = 'Left'
                leftMove[i-1] = 'B'
                if (CalculateDistance(leftMove, backboard, frontboard, winState) < d):
                    return leftMove, val, direction
                else:
                    deltaE = CalculateDistance(leftMove, backboard, frontboard, winState) - d
                    acceptProbability = min(math.exp(deltaE / temp), 1)
                    if random.random() <= acceptProbability:
                        return leftMove, val, direction
        else:    
            if ((i+1)%sideLength != 0 and isinstance((anyBoard[i+1]), int)):
                rightMove = anyBoard
                rightMove[i] = anyBoard[i+1]
                val = rightMove[i]
                direction = 'Right'
                rightMove[i+1] = 'B'
                if CalculateDistance(rightMove, backboard, frontboard, winState) < d:
                    return rightMove, val, direction
                else:
                    deltaE = CalculateDistance(rightMove, backboard, frontboard, winState) - d
                    acceptProbability = min(math.exp(deltaE / temp), 1)
                    if random.random() <= acceptProbability:
                        return rightMove, val, direction
    


def solution_SimulatedAnnealing(board, backboard, frontboard, winState, arg_run_time):
    # the success rate will increase by increasing the maxRound
    maxRound = 10000000
    board_size = len(board)
    if board_size < 4:
        NumberOfRuns = arg_run_time
    else:
        NumberOfRuns = arg_run_time / 2.0
    timePerRound = arg_run_time / NumberOfRuns
    count = 0
    originalboard = board
    start = time.perf_counter()
    newrunstart = time.perf_counter()
    solutionCost = 0
    temp = len(board)
    decay = 0.9
    newcount = 0
    moves = ['Start Solution', 'First Move:']

    while True:
        currenttime = time.perf_counter()
        endtime = abs(start - currenttime)
        runend = abs(newrunstart - currenttime)

        collisionNum = CalculateDistance(board, backboard, frontboard, winState)

        if collisionNum == 0:
            length = len(moves) - 1
            # for i in range(0, length, 2):
            #     print(moves[i] + ' ' + moves[i+1])
            #print(moves)
            print("Move Count (Total Nodes Visited)")
            print (count)
            print("Moves in Solution (Node Depth)")
            print(newcount)
            print("Branching Factor")
            print((count)**(1/newcount))
            print("Solution Cost")
            print(solutionCost)
            print("Final Board")
            return [board, arg_run_time, count, newcount, solutionCost, (count)**(1/newcount), endtime]
        if (newcount > 1000 or runend > timePerRound):
            board = originalboard
            newrunstart = time.perf_counter()
            solutionCost = 0
            newcount = 0
            moves = ['Start Solution', 'First Move:']

        board, val, direction = hillClimbing(board, backboard, frontboard, winState, temp)
        solutionCost += val
        movestring = str(val)
        moves.append(movestring)
        moves.append(direction)
        count += 1
        newcount += 1
        temp = temp * decay

        if(count >= maxRound or endtime > arg_run_time):
            print("Could not complete in time")
            return [board, arg_run_time,count, newcount, solutionCost, (count)**(1/newcount), "N/A"]


if __name__ == '__main__':
    BOARD = sys.argv[1]
    RUN_TIME = sys.argv[2]

    main(BOARD, RUN_TIME)