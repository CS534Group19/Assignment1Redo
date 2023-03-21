import threading
from time import sleep
import math
import copy

csv_file = "./documentation/test_boards/board1.csv"

START_STATE =                   [[1, 3, 6], [4, 2, 0], [7, 5, 9]]
START_STATE_ALTERED =           [[1, 3, 6], [4, 0, 2], [7, 5, 9]]
GOAL_STATE  =                   [[1, 2, 3], [4, 5, 6], [7, 9, 0]]
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
        return 0
        # TODO - Greedy
        # calc_total_manhattan_distance(whole_board, heuristic_uses_weights_TF)
    else:
        return 0

H_TYPE = "Sliding"
HVAL_USES_WEIGHTS = True

class BoardState:
    def __init__(self, current_board_state, parent_board, g, heuristic_type, heuristic_uses_weights_TF):
        self.current_board_state = current_board_state
        self.parent = parent_board
        self.g = g
        self.h = heuristic(current_board_state, heuristic_type, heuristic_uses_weights_TF)
        self.f = self.g + self.h

    def __str__(self):
        return str(self.current_board_state)

FRONTIER = [BoardState(START_STATE, None, 0, H_TYPE, HVAL_USES_WEIGHTS)]
VISITED = []

# Finds the state in the frontier with the lowest f-value
def get_state_with_lowest_fval():
    smallest_state_fval_so_far = 99999999999999
    smallest_state_so_far = None
    for board in FRONTIER:
        if board.f < smallest_state_fval_so_far:
            smallest_state_fval_so_far = board.f
            smallest_state_so_far = board
    return smallest_state_so_far

# Takes a board_state and returns a list of boards which are possible from the given state's blanks
# TODO TODO TODO
def get_all_possible_states_from_current_state(board_state):
    states = []
    for row in range(N):
        for col in range(N):
            if board_state.current_board_state[row][col] == 0:

                # Up
                delta_y = row + 1
                if delta_y >= 0 and delta_y < N:
                    if board_state.current_board_state[delta_y][col] != 0:
                        new_board_state = copy.deepcopy(board_state.current_board_state)
                        new_board_state[row][col] = new_board_state[delta_y][col]
                        new_board_state[delta_y][col] = 0
                        states.append(BoardState(new_board_state, board_state, board_state.g + new_board_state[row][col], H_TYPE, HVAL_USES_WEIGHTS))
                # Down
                delta_y = row - 1
                if delta_y >= 0 and delta_y < N:
                    if board_state.current_board_state[delta_y][col] != 0:
                        new_board_state = copy.deepcopy(board_state.current_board_state)
                        new_board_state[row][col] = new_board_state[delta_y][col]
                        new_board_state[delta_y][col] = 0
                        states.append(BoardState(new_board_state, board_state, board_state.g + new_board_state[row][col], H_TYPE, HVAL_USES_WEIGHTS))
                # Left
                delta_x = col - 1
                if delta_x >= 0 and delta_x < N:
                    if board_state.current_board_state[row][delta_x] != 0:
                        new_board_state = copy.deepcopy(board_state.current_board_state)
                        new_board_state[row][col] = new_board_state[row][delta_x]
                        new_board_state[row][delta_x] = 0
                        states.append(BoardState(new_board_state, board_state, board_state.g + new_board_state[row][col], H_TYPE, HVAL_USES_WEIGHTS))
                # Right
                delta_x = col + 1
                if delta_x >= 0 and delta_x < N:
                    if board_state.current_board_state[row][delta_x] != 0:
                        new_board_state = copy.deepcopy(board_state.current_board_state)
                        new_board_state[row][col] = new_board_state[row][delta_x]
                        new_board_state[row][delta_x] = 0
                        states.append(BoardState(new_board_state, board_state, board_state.g + new_board_state[row][col], H_TYPE, HVAL_USES_WEIGHTS))
    return states 

def calc_the_move_between_two_states(board_state_from, board_state_to):
    
    # Base move value
    move = "Moved "
    
    for row in range(N):
        for col in range(N):
            if board_state_from.current_board_state[row][col] != board_state_to.current_board_state[row][col] and board_state_to.current_board_state[row][col] != 0:
    
                # Add the tile value to the string
                move += str(board_state_to.current_board_state[row][col]) + " "

                # Add the directional portion to the string
                if row - 1 >= 0 and board_state_from.current_board_state[row][col] == board_state_to.current_board_state[row - 1][col]:
                    move += "up"
                    break
                elif row + 1 <= (N - 1) and board_state_from.current_board_state[row][col] == board_state_to.current_board_state[row + 1][col]:
                    move += "down"
                    break
                elif col - 1 >= 0 and board_state_from.current_board_state[row][col] == board_state_to.current_board_state[row][col - 1]:
                    move += "left"
                    break
                elif col + 1 <= (N - 1) and board_state_from.current_board_state[row][col] == board_state_to.current_board_state[row][col + 1]:
                    move += "right"
                    break
                else:
                    continue
    return move

def backtrack_path_from_current(board_state):
    path = []
    while not(board_state.parent == None):
        print("found parent")
        path.append(calc_the_move_between_two_states(board_state.parent, board_state))
        board_state = board_state.parent
    path.reverse()
    return path

def A_Star():
    while len(FRONTIER) > 0:
        current_board = get_state_with_lowest_fval()
        if current_board.current_board_state == GOAL_STATE:
            return backtrack_path_from_current(current_board)
        FRONTIER.remove(current_board)
        VISITED.append(current_board)
        for child_state in get_all_possible_states_from_current_state(current_board):
            if child_state in VISITED:
                continue
            if not(child_state in FRONTIER):
                FRONTIER.append(child_state)

#output_file_name = "C:\\Users\\essmi\\OneDrive\\Desktop\\Output.txt"
#fo = open(output_file_name, "w")
#PATH = A_Star()
#fo.write(", ".join(PATH))
#fo.close()


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

    print("The start board: \n", START_STATE)

    startchildren = get_all_possible_states_from_current_state(BoardState(START_STATE, None, 0, H_TYPE, HVAL_USES_WEIGHTS))
    print("# of children it has :", len(startchildren))

    print("Test of board movement: ")
    print(calc_the_move_between_two_states(BoardState(START_STATE, None, 0, H_TYPE, HVAL_USES_WEIGHTS), 
                                           BoardState(START_STATE_ALTERED, None, 0, H_TYPE, HVAL_USES_WEIGHTS)))
    
    print(backtrack_path_from_current(startchildren[0]))


