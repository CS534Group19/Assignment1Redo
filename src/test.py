from board import Board

csv_file = "./documentation/test_boards/board1.csv"

board = Board(csv_file)

print(str(board.find_goal_state()))