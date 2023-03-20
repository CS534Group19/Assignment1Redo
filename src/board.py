import csv
from copy import deepcopy


class Board():
    def __init__(self, csv_file=None, array_board=None, move_title=None):
        self.csv_file = csv_file
        if self.csv_file is not None:
            self.board = self.create_2D_board()
        else:
            self.board = array_board
        self.side_length = len(self.board)
        self.possible_moves = []
        self.move_title = move_title

    def create_2D_board(self):
        board = []
        # TODO is this encoding proper?
        with open(self.csv_file, 'r', encoding='utf-8-sig') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                temp = []
                for value in row:
                    if value == "B":
                        temp.append(0)
                    else:
                        temp.append(int(value))
                board.append(temp)
        return board

    def create_1D_board(self):
        board_1D = []
        for row in self.board:
            for value in row:
                board_1D.append(value)
        return board_1D

    def make_2D(self, sorted_1D: list[int]):
        """
        ### Parameters
        - sorted_1D: a sorted 1D representation of a board

        ### Returns
        - 2D array of the sorted board
        """
        goal_1D = sorted_1D
        goal_2D = []
        index = 0
        for i in range(self.side_length):
            temp_row = []
            for j in range(self.side_length):
                temp_row.append(goal_1D[index])
                index += 1
            goal_2D.append(temp_row)
        return goal_2D

    def find_goal_state(self):
        """Returns a 2D array created from a re-arranged sorted 1D array with all zeros in the bottom right
        """
        sorted_board = sorted(self.create_1D_board())
        end_zeroes = 0
        for i in range(len(sorted_board)):
            if sorted_board[i] == 0:
                end_zeroes = i
        zero_list = sorted_board[0: end_zeroes + 1]
        sorted_board = sorted_board[end_zeroes + 1:] + zero_list
        return self.make_2D(sorted_board)

    # Neighbor tuple form (0_x, 0_y, neighbor_x, neighbor_y)
    def set_possible_moves(self) -> list[tuple]:
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    # Up
                    delta_y = row+1
                    if delta_y >= 0 and delta_y < len(self.board):
                        if self.board[delta_y][col] != 0:
                            moves.append((col, row, col, delta_y))
                    # Down
                    delta_y = row-1
                    if delta_y >= 0 and delta_y < len(self.board):
                        if self.board[delta_y][col] != 0:
                            moves.append((col, row, col, delta_y))
                    # Left
                    delta_x = col-1
                    if delta_x >= 0 and delta_x < len(self.board):
                        if self.board[row][delta_x] != 0:
                            moves.append((col, row, delta_x, row))
                    # Right
                    delta_x = col+1
                    if delta_x >= 0 and delta_x < len(self.board):
                        if self.board[row][delta_x] != 0:
                            moves.append((col, row, delta_x, row))
        # A move is (0_x, 0_y, Neighbor_x, Neighbor_y)
        self.possible_moves = moves

    @staticmethod
    def create_children(list_moves, parent_board):
        children = []
        for move in list_moves:
            current_board = deepcopy(parent_board.board)
            x_0, y_0, neighbor_x, neighbor_y = move

            neighbor_value = current_board[neighbor_y][neighbor_x]
            # Swap 0 with neighbor_value
            current_board[y_0][x_0] = neighbor_value
            current_board[neighbor_y][neighbor_x] = 0

            move_string = ""
            # Compute string representation of the board move
            if (neighbor_y-y_0) == 1 and (neighbor_x-x_0) == 0:
                move_string = f"Moved {parent_board.board[neighbor_y][neighbor_x]} up"
            elif (neighbor_y-y_0) == -1 and (neighbor_x-x_0) == 0:
                move_string = f"Moved {parent_board.board[neighbor_y][neighbor_x]} down"
            elif (neighbor_x-x_0) == 1 and (neighbor_y-y_0) == 0:
                move_string = f"Moved {parent_board.board[neighbor_y][neighbor_x]} left"
            elif (neighbor_x-x_0) == -1 and (neighbor_y-y_0) == 0:
                move_string = f"Moved {parent_board.board[neighbor_y][neighbor_x]} right"

            temp_board = Board(csv_file=None, array_board=current_board, move_title=move_string)
            children.append((temp_board, neighbor_value))
        return children

    def __str__(self):
        return str(self.board)
    
def get_coords_for_val(board: list[list[int]], val: int):
    """Static method to find the (x,y) coordinates of the provided value
    ### Parameters
    - board: a 2D array representing a board state
    - val: the value being searched for

    ### Returns
    Either an (x,y) tuple if the value is on the board or -1 if it wasn't found
    """
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == val:
                return (x, y)
    return -1

def calculate_manhattan_dist_for_value(current_board: list[list[int]], goal_board: list[list[int]], val: int, weighted: bool) -> int:
    """Static method to compute the Manhattan distance for a given value
    ### Parameters
    - current_board: the current state of the board
    - goal_board: the goal state for the computation
    - val: the value the calculation is based on

    ### Returns
    - The integer Manhattan distance for the value to its goal location or -1 if the value isn't on the board
    """
    # Find (x,y) coords for all current positions
    current_coords: tuple = get_coords_for_val(current_board, val)
    goal_coords: tuple = get_coords_for_val(goal_board, val)
    if current_coords == -1 or goal_coords == -1:
        return -1
    else:
        if weighted == True:
            return abs(current_coords[0] - goal_coords[0]) + abs(current_coords[1] - goal_coords[1]) * val
        else:
            return abs(current_coords[0] - goal_coords[0]) + abs(current_coords[1] - goal_coords[1])

def getHVal(board_obj: Board, goal: list[list[int]]) -> int: # sliding heuristic
    """Static method to find the total heuristic value of a given board
    ### Parameters
    - board_obj: a Board object to be fitted with a heuristic value

    ### Returns
    - total: the heuristic cost of the board
    """
    total: int = 0
    for i in range(1, len(board_obj.board)**2):
        # TODO implement weighted command line arg
        manhattan_distance = calculate_manhattan_dist_for_value(board_obj.board, goal, i, False)
        if manhattan_distance != -1:
            total += manhattan_distance
    return total
