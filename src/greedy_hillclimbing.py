from initialization import Initialization
from board_state import BoardState
import time
from time import sleep
import threading

start_file = "D:\\WPI\\Sophomore Year\\CS534\\Assignment1Redo\\documentation\\test_boards\\4x4x2.csv"

HEURISTIC = "Sliding"
WEIGHTED = True
# Runtime in seconds
RUN_TIME = 20
RESTARTS = 1000

new_board = Initialization(start_file)
board_state = BoardState(new_board.board, new_board.goal, HEURISTIC, WEIGHTED)

reached_goal = False
open = [board_state]
closed = []
current_state = board_state


class HillclimbingThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()

    def hillclimbing(self):
        global reached_goal
        global open
        global closed
        global current_state
        global trial_time
        global trial_time_total

        trial_time = RUN_TIME / RESTARTS
        trial_counter = 0
        trial_time_total = 0.0

        start_time = time.perf_counter()
        current_time = time.perf_counter()

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
            if (current_time - start_time < RUN_TIME):
                trial_time_total = 0.0
                trial_counter += 1
                
                trial_start_time = time.perf_counter()

                current_state = open.pop()
                current_time = time.perf_counter()

                
                children = current_state.get_children()
                children.sort(key=lambda x: x.h)
                open.append(children[0])
                closed.append(current_state)

                trial_end_time = time.perf_counter()
                trial_time_total += trial_end_time - trial_start_time
            else:
                print("Out of time")
                break
            current_time = time.perf_counter()

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
