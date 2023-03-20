from board import *
import threading
from time import sleep
import heapq

csv_file = "./documentation/test_boards/board1.csv"

board = Board(csv_file)
board.set_possible_moves()

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
    
    #heuristic function
    def manhattan_distance(self, goal, board):
        pass

    #The main A* algorithm
    def a_star(self, start, goal):
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
                if (child) not in cost_so_far or new_cost < cost_so_far[child]:
                    cost_so_far[child] = new_cost
                    priority = new_cost + self.manhattan_distance(goal, child)
                    heapq.heappush(frontier, (priority, child))
                    came_from[child] = current

        path = [goal]
        while path[-1] != start:
            path.append(came_from[path[-1]])
        path.reverse()

        return path


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
