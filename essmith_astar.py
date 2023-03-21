import threading
from time import sleep
import math

csv_file = "./documentation/test_boards/board1.csv"

START_STATE =        [[1, 3, 6], [4, 2, 0], [7, 5, 9]]
GOAL_STATE  =        [[1, 2, 3], [4, 5, 6], [7, 9, 0]]
N = len(START_STATE)

# Runtime in seconds
RUN_TIME = 5

# Calculates the total manhattan distances for each tile in the board
#   board_tile      -   the current board tile
#   x               -   the x cartesian coordinate of the board_tile
#   y               -   the y cartesian coordinate of the board_tile
#   weighted_TF     -   whether the manhattan distance should use the tile weight as well
def calc_manhattan_distance(board_tile, x, y, weighted_TF):
    if board_tile == 0:
        return 0
    for row in range(N):
        for col in range(N):
            if GOAL_STATE[row][col] == board_tile:
                if weighted_TF == True:
                    return board_tile * (abs(x - row) + abs(y - col))
                else:
                    return (abs(x - row) + abs(y - col))

# Calculates the total manhattan distances for each tile in the board
#   whole_board     -   the board
#   weighted_TF     -   whether the manhattan distance should use the tile weights as well
def calc_total_manhattan_distance(whole_board, weighted_TF):
    total_manhattan_distance = 0
    for row in range(N):
        for col in range(N):
            current_tile_of_board = whole_board[row][col]
            total_manhattan_distance += calc_manhattan_distance(current_tile_of_board, row, col, weighted_TF)    
    return total_manhattan_distance

# TODO
def heuristic(whole_board, h_type):
    """
    Probably define h_type as number, each for preferred heuristic type
    """
    return 0




"""
run_thread = AStarThread(board, goal_state)
run_thread.daemon = True

print(f"Please wait {RUN_TIME} seconds...")
run_thread.start()

sleep(RUN_TIME)

run_thread.stop()
run_thread.join()
"""

"""
Testing stuff :)
"""
DEBUG = True
if DEBUG == True:
    print(N)

    unweightedManhatTest = calc_total_manhattan_distance(START_STATE, False)
    weightedManhatTest = calc_total_manhattan_distance(START_STATE, True)

    print("Total Unweighted Manhattan of Start State equals: ", unweightedManhatTest)
    print("Total Unweighted Manhattan of Start State equals: ", weightedManhatTest)