from board import *

csv_file = "./documentation/test_boards/board1.csv"

board = Board(csv_file)
board.set_possible_moves()
goal_state = board.find_goal_state()

print(f"Current h value for start board: {getHVal(board, goal_state)}\n")

children = Board.create_children(board.possible_moves, board)

for child in children:
    print(getHVal(child[0], goal_state))

a = [[1,2], [3,4]]
b = [[1,2], [3,4]]

print(a==b)