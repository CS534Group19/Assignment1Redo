from initialization import Initialization
from board_state import BoardState
import time
from time import sleep
import threading
import random

start_file = "D:\\WPI\\Sophomore Year\\CS534\\Assignment1Redo\\documentation\\test_boards\\4x4x2.csv"

HEURISTIC = "Sliding"
WEIGHTED = True
# Runtime in seconds
RUN_TIME = 30
DEPTH = 3

new_board = Initialization(start_file)
board_state = BoardState(new_board.board, new_board.goal, HEURISTIC, WEIGHTED)

reached_goal = False
current_state: BoardState = board_state
closed = []


class HillclimbingThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()

    def hillclimbing(self):
        global reached_goal
        global current_state
        global closed

        start_time = time.perf_counter()
        while not reached_goal and not self._stop_event.is_set():
            if current_state.board_array == board_state.goal_array:
                reached_goal = True
                moves = []
                effort_total = 0
                final_depth = current_state.node_depth
                while current_state.parent is not None:
                    effort_total += current_state.effort
                    moves.append(current_state.move_title)
                    current_state = current_state.parent
                moves.reverse()
                for move in moves:
                    print(move)

                print(f"\nNodes expanded: {len(closed)}")
                print(f"Moves required: {len(moves)}")
                print(f"Solution Cost: {effort_total}")
                if final_depth != 0:
                    print(
                        f"Estimated branching factor {len(closed)**(1/final_depth):0.3f}")
                end_time = time.perf_counter()
                print(f"\nSearch took {end_time - start_time:0.4f} seconds")
                break

            
            children = current_state.get_children()
            closed.append(current_state)

            best = current_state
            for child in children:
                for i in range(DEPTH):
                    if child.h < best.h:
                        best = child
                    else:
                        break

    def run(self):
        lock = threading.Lock()
        with lock:
            self.hillclimbing()

    def stop(self):
        self._stop_event.set()


run_thread = HillclimbingThread()
run_thread.daemon = True

print(f"Please wait {RUN_TIME} seconds...")

reached_goal = False
run_thread.start()

sleep(RUN_TIME)

run_thread.stop()
run_thread.join()

if not reached_goal:
    print("\nGoal not reached...")
    print("Printing current data.\n")
    moves = []
    effort_total = 0
    final_depth = current_state.node_depth
    while current_state.parent is not None:
        effort_total += current_state.effort
        moves.append(current_state.move_title)
        current_state = current_state.parent
    moves.reverse()
    # for move in moves:
    #     print(move)

    print(f"Nodes expanded: {len(closed)}")
    print(f"Moves required: {len(moves)}")
    print(f"Solution Cost: {effort_total}")
    if final_depth != 0:
        print(
            f"Estimated branching factor {len(closed)**(1/final_depth):0.3f}")
