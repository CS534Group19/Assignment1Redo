import os
import csv

from initialization import Initialization
from board_state import BoardState
import astar
from hillclimbing import *

# A* Tests
HEURISTIC_OPTIONS = ["Sliding", "Greedy"]
WEIGHTED_OPTIONS = ["True", "False"]

Assignment1RedoDir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
DATA_DIR = f"{Assignment1RedoDir}\\documentation\\data"

def clear_data_dir():
    for file in os.listdir(DATA_DIR):
        os.remove(os.path.join(DATA_DIR, file))

# write tests for hillclimbing here following the below format using the same csv files
# for each csv file, run each for 1-15 seconds each
# with open(f"{DATA_DIR}\\data_hillclimbing.csv", "w", newline="") as data_file:
#     data_writer = csv.writer(data_file)
#     data_writer.writerow(["File Name", "Runtime", "Nodes Expanded", "Moves Required", "Solution Cost", "Estimated Branching Factor", "Search Time"])
#     for file in os.listdir(Assignment1RedoDir + "\\documentation\\test_boards"):
#         print(file)
#         i = 20
#         while i < 61:
#             data_writer.writerow([file] + main(f"{Assignment1RedoDir}\\documentation\\test_boards\\{file}", i)[1:])
#             i += 5

# test a 4x4 board with hillclimbing
with open(f"{DATA_DIR}\\data_hillclimbing_4x4.csv", "w", newline="") as data_file:
    data_writer = csv.writer(data_file)
    data_writer.writerow(["File Name", "Runtime", "Nodes Expanded", "Moves Required", "Solution Cost", "Estimated Branching Factor", "Search Time"])
    file = Assignment1RedoDir + "\\documentation\\test_boards\\4x4x2.csv"
    print(file)
    for i in range(10):
        data_writer.writerow([file] + main(file, 120)[1:])

# with open(f"{DATA_DIR}\\data.csv", "w", newline="") as data_file:
#     data_writer = csv.writer(data_file)
#     data_writer.writerow(["File Name", "Heuristic", "Weighted", "Nodes Expanded", "Moves Required", "Solution Cost", "Estimated Branching Factor", "Search Time"])
#     for file in os.listdir(Assignment1RedoDir + "\\documentation\\test_boards"):
#         for heuristic in HEURISTIC_OPTIONS:
#             for weighted in WEIGHTED_OPTIONS:
#                 print(file)
#                 new_board = Initialization(f"{Assignment1RedoDir}\\documentation\\test_boards\\{file}")
#                 board_state = BoardState(new_board.board, new_board.goal, heuristic, weighted)
#                 data_writer.writerow([file, heuristic, weighted] + astar.a_star(board_state))

# # testing just 4x4x2.csv 10 times with same criteria as above
# with open(f"{DATA_DIR}\\data_4x4x2_sliding_weighted.csv", "w", newline="") as data_file:
#     data_writer = csv.writer(data_file)
#     data_writer.writerow(["File Name", "Heuristic", "Weighted", "Nodes Expanded",
#                          "Moves Required", "Solution Cost", "Estimated Branching Factor", "Search Time"])
#     for i in range(10):
#         new_board = Initialization(
#             f"{Assignment1RedoDir}\\documentation\\test_boards\\4x4x2.csv")
#         board_state = BoardState(
#             new_board.board, new_board.goal, "Sliding", "True")
#         data_writer.writerow(
#             ["4x4x2.csv", "Sliding", "True"] + astar.a_star(board_state))

# # same test as above but with 4x4x2.csv 10 times with greedy heuristic weighted
# with open(f"{DATA_DIR}\\data_4x4x2_greedy_weighted.csv", "w", newline="") as data_file:
#     data_writer = csv.writer(data_file)
#     data_writer.writerow(["File Name", "Heuristic", "Weighted", "Nodes Expanded",
#                          "Moves Required", "Solution Cost", "Estimated Branching Factor", "Search Time"])
#     for i in range(10):
#         new_board = Initialization(
#             f"{Assignment1RedoDir}\\documentation\\test_boards\\4x4x2.csv")
#         board_state = BoardState(
#             new_board.board, new_board.goal, "Greedy", "True")
#         data_writer.writerow(
#             ["4x4x2.csv", "Greedy", "True"] + astar.a_star(board_state))

# # same test as above but with 4x4x2.csv 10 times with sliding heuristic unweighted
# with open(f"{DATA_DIR}\\data_4x4x2_sliding_unweighted.csv", "w", newline="") as data_file:
#     data_writer = csv.writer(data_file)
#     data_writer.writerow(["File Name", "Heuristic", "Weighted", "Nodes Expanded",
#                          "Moves Required", "Solution Cost", "Estimated Branching Factor", "Search Time"])
#     for i in range(10):
#         new_board = Initialization(
#             f"{Assignment1RedoDir}\\documentation\\test_boards\\4x4x2.csv")
#         board_state = BoardState(
#             new_board.board, new_board.goal, "Sliding", "False")
#         data_writer.writerow(
#             ["4x4x2.csv", "Sliding", "False"] + astar.a_star(board_state))

# # same test as above but with 4x4x2.csv 10 times with greedy heuristic unweighted
# with open(f"{DATA_DIR}\\data_4x4x2_greedy_unweighted.csv", "w", newline="") as data_file:
#     data_writer = csv.writer(data_file)
#     data_writer.writerow(["File Name", "Heuristic", "Weighted", "Nodes Expanded",
#                          "Moves Required", "Solution Cost", "Estimated Branching Factor", "Search Time"])
#     for i in range(10):
#         new_board = Initialization(
#             f"{Assignment1RedoDir}\\documentation\\test_boards\\4x4x2.csv")
#         board_state = BoardState(
#             new_board.board, new_board.goal, "Greedy", "False")
#         data_writer.writerow(
#             ["4x4x2.csv", "Greedy", "False"] + astar.a_star(board_state))


