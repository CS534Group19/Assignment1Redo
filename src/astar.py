from initialization import Initialization
from board_state import BoardState
import time
from time import sleep
import threading

start_file = ".\\documentation\\test_boards\\4x4x2.csv"

HEURISTIC = "Greedy"
WEIGHTED = True
# Runtime in seconds
RUN_TIME = 4

new_board = Initialization(start_file)
board_state = BoardState(new_board.board, new_board.goal, HEURISTIC, WEIGHTED)

reached_goal = False
open = [board_state]
closed = []
current_state: BoardState


class AStarThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()

    def a_star(self):
        global reached_goal
        global open
        global closed
        global current_state

        start_time = time.perf_counter()

        while True and not self._stop_event.is_set():
            current_state = open.pop(0)
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
            for child in children:
                # Speeds up processing by not checking the child if it's already been checked
                if child.board_array in [board.board_array for board in closed]:
                    continue
                if child.board_array not in [board.board_array for board in open]:
                    open.append(child)
            closed.append(current_state)
            open.sort(key=lambda x: x.f)

    def run(self):
        lock = threading.Lock()
        with lock:
            self.a_star()

    def stop(self):
        self._stop_event.set()


run_thread = AStarThread()
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
