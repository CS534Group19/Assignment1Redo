from board import Board
import threading
from time import sleep
import heapq

csv_file = "./documentation/test_boards/board1.csv"

board = Board(csv_file)

# Runtime in seconds
RUN_TIME = 5

class AStarThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()

    #define costs for moves
    def get_cost(self, child_board, move):
        tile_x,tile_y = move[2],move[3]
        return child_board[tile_y][tile_x]


    def a_star(self, grid, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}
        while frontier:
            current = heapq.heappop(frontier)[1]
            if current == goal:
                break

            for child in self.get_children(current):
                new_cost = cost_so_far[current] + self.get_cost(child[0], child[1])

    


    def run(self):
        lock = threading.Lock()
        with lock:
            # TODO write AStar here
            pass

    def stop(self):
        self._stop_event.set()

    

run_thread = AStarThread()
run_thread.daemon = True
run_thread.start()

print(f"Please wait {RUN_TIME} seconds...")
sleep(RUN_TIME)

run_thread.stop()
run_thread.join()
