from board import Board
import threading
from time import sleep

csv_file = "./documentation/test_boards/board1.csv"

board = Board(csv_file)

# Runtime in seconds
RUN_TIME = 5

class BoardThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()

    def run(self):
        lock = threading.Lock()
        with lock:
            # TODO write Greedy here
            pass

    def stop(self):
        self._stop_event.set()

run_thread = BoardThread()
run_thread.daemon = True
run_thread.start()

print(f"Please wait {RUN_TIME} seconds...")
sleep(RUN_TIME)

run_thread.stop()
run_thread.join()
