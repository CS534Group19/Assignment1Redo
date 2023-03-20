from board import *
import threading
from time import sleep
import heapq

csv_file = "./documentation/test_boards/board1.csv"

board = Board(csv_file)
board.set_possible_moves()
goal_state = board.find_goal_state()

# Runtime in seconds
RUN_TIME = 5


class AStarThread(threading.Thread):
    def __init__(self, board, goal):
        threading.Thread.__init__(self)
        self._stop_event = threading.Event()
        self.board = board
        self.goal = goal

    # The main A* algorithm
    def a_star(self, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}

        while frontier:
            current = heapq.heappop(frontier)[1]
            if current == goal:
                break

            for child in Board.create_children(self.board.possible_moves, self.board):
                new_cost = cost_so_far[current] + child[1]
                if (child[0]) not in cost_so_far or new_cost < cost_so_far[child[0]]:
                    cost_so_far[child[0]] = new_cost
                    priority = new_cost + getHVal(child[0], goal_state)
                    # TODO fix heappush error
                    heapq.heappush(frontier, (priority, child[0]))
                    came_from[child[0]] = current

        path = [goal]
        while path[-1] != start:
            path.append(came_from[path[-1]])
        path.reverse()

        return path

    def run(self):
        lock = threading.Lock()
        with lock:
            path = self.a_star(self.board, self.goal)
            for board in path:
                print(board.move_title)

    def stop(self):
        self._stop_event.set()


run_thread = AStarThread(board, goal_state)
run_thread.daemon = True

print(f"Please wait {RUN_TIME} seconds...")
run_thread.start()

sleep(RUN_TIME)

run_thread.stop()
run_thread.join()
