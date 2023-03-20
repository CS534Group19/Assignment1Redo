from board import *
import threading
from time import sleep

csv_file = "./documentation/test_boards/board1.csv"

board = Board(csv_file)
board.set_possible_moves()

# Runtime in seconds
RUN_TIME = 5

class GreedyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()

    def greedy(self):
        pass

    def run(self):
        lock = threading.Lock()
        with lock:
            self.greedy()

    def stop(self):
        self._stop_event.set()

run_thread = GreedyThread()
run_thread.daemon = True
run_thread.start()

print(f"Please wait {RUN_TIME} seconds...")
sleep(RUN_TIME)

run_thread.stop()
run_thread.join()
