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

# TODO - GREEDY
def heuristic(whole_board, heuristic_type, heuristic_uses_weights_TF):
    if heuristic_type == "Sliding":
        return calc_total_manhattan_distance(whole_board, heuristic_uses_weights_TF)
    elif heuristic_type == "Greedy":
        return None
        # TODO - Greedy
        # calc_total_manhattan_distance(whole_board, heuristic_uses_weights_TF)
    else:
        return 0

class BoardState:
    def __init__(self, current_board_state, parent_board, g, heuristic_type, heuristic_uses_weights_TF):
        self.current_board_state = current_board_state
        self.parent = parent_board
        self.g = g
        self.h = heuristic(current_board_state, heuristic_type, heuristic_uses_weights_TF)
        self.f = self.g + self.h

H_TYPE = "Greedy"
HVAL_USES_WEIGHTS = True
FRONTIER = [BoardState(START_STATE, None, 0, H_TYPE, HVAL_USES_WEIGHTS)]
VISITED = []

# Finds the state in the frontier with the lowest f-value
def get_state_with_lowest_fval():
    smallest_state_fval_so_far = math.inf()
    smallest_state_so_far = None
    for board in FRONTIER:
        if board.f < smallest_state_fval_so_far:
            smallest_state_fval_so_far = board.f
            smallest_state_so_far = board
    return smallest_state_so_far

# Takes a board_state and returns a list of boards which are possible from the given state's blanks
def get_all_possible_states_from_current_state(board_state):
    states = []
    for row in range(N):
        for col in range(N):
            if board_state[row][col] == 0:
                # Up
                delta_y = row+1
                if delta_y >= 0 and delta_y < N:
                    if board_state[delta_y][col] != 0:
                        states.append((col, row, col, delta_y))
                # Down
                delta_y = row-1
                if delta_y >= 0 and delta_y < N:
                    if board_state[delta_y][col] != 0:
                        states.append((col, row, col, delta_y))
                # Left
                delta_x = col-1
                if delta_x >= 0 and delta_x < N:
                    if board_state[row][delta_x] != 0:
                        states.append((col, row, delta_x, row))
                # Right
                delta_x = col+1
                if delta_x >= 0 and delta_x < N:
                    if board_state[row][delta_x] != 0:
                        states.append((col, row, delta_x, row))   
    return states 

def calc_the_move_between_two_states(origin_state, destination_state):
    
    # Base move value
    move = "Moved "
    
    for row in range(N):
        for col in range(N):
            if origin_state.current_board_state[row][col] != destination_state.current_board_state[row][col] and destination_state.current_board_state[row][col] != 0:
    
                # Add the tile value to the string
                move += destination_state.current_board_state[row][col] + " "

                # Add the directional portion to the string
                if row - 1 >= 0 and origin_state.current_board_state[row][col] == destination_state.current_board_state[row - 1][col]:
                    move += "up"
                elif row + 1 <= (N - 1) and origin_state.current_board_state[row][col] == destination_state.current_board_state[row + 1][col]:
                    move += "down"
                elif col - 1 >= 0 and origin_state.current_board_state[row][col] == destination_state.current_board_state[row][col - 1]:
                    move += "left"
                else: 
                    move += "right"
                break       
    return move


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