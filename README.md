# Assignment1Redo
Another attempt at Assignment 1
### Group 19
- Michael Alicea, malicea2@wpi.edu
- Cutter Beck, cjbeck@wpi.edu
- Jeffrey Davis, jrdavis2@wpi.edu
- Oliver Shulman, ohshulman@wpi.edu
- Edward Smith, essmith@wpi.edu

-------------------------------------------------------------------------------------------------------------------------------------
## PROGRAM SPECIFICATIONS
-------------------------------------------------------------------------------------------------------------------------------------
- This program is coded in Python 3.11.2, but higher versions will work as well
- Using the UTF-8-sig Encoding (based on Professor Beck's example files)
- This program can be run using the terminal command permutations, one each for project part
-------------------------------------------------------------------------------------------------------------------------------------
## PROGRAM EXECUTION
------------------------------------------------------------------------------------------------------------------------------------- 
### RUNNING PART 1 - A* Search
1. To run A* Search:
    1. Run the following from the `src` directory
        1. COMMAND: `python astar.py path_to_board.csv heuristic tile_weight?`
            - path_to_board.csv: the path location of the board CSV file the algorithm will search
            - heuristic: one of `Sliding` or `Greedy`
                - **`Sliding` will run this version of AStar for Part 1**
            - tile_weight?: one of `True` or `False`
                - This will run the A* Search with either a weighted heuristic (`True`) or an unweighted heuristic (`False`)
2. Output from A* Search:
    1. Moves
        1. The exact moves necessary to solve the board state
    2. Nodes Expanded
        1. The total number of nodes expanded during the search for the goal
    3. Moves Required
        1. total number of moves required to reach the goal
    4. Solution Cost
        1. The total cost of the moves adjusted for the tile weights
    5. Estimated Branching Factor
        1. The average number of branches from a parent node to a child node during the search. This is computed with the formula (total # of expanded nodes) ^ (1 / solution node depth)
-------------------------------------------------------------------------------------------------------------------------------------
### RUNNING PART 2 - Hill Climbing
1. To run Hill Climbing:
    1. Run from command line
        1. COMMAND: `python hillclimbing.py path_to_board.csv time`
            - path_to_board.csv: the path location of the board CSV file the algorithm will search
            - time: a value in seconds, can be an integer or float as it is cast to float during execution
2. Output from Hill Climbing:
    1. Moves
        1. The exact moves necessary to solve the board state
    2. Nodes Expanded
        1. The total number of nodes expanded during the search for the goal
    3. Moves Required
        1. The total number of moves required to reach the goal
    4. Solution Cost
        1. The total cost of the moves adjusted for the tile weights
    5. Estimated Branching Factor
        1. The average number of branches from a parent node to a child node during the search. This is computed with the formula (total # of expanded nodes) ^ (1 / solution node depth)
-------------------------------------------------------------------------------------------------------------------------------------
### RUNNING PART 3 - Modified A* Search
1. To run Modifed A* Search:
    1. Run from command line
        1. COMMAND: `python astar.py path_to_board.csv heuristic tile_weight?`
            - path_to_board.csv: the path location of the board CSV file the algorithm will search
            - heuristic: one of `Sliding` or `Greedy`
                - **`Greedy` will run this modified version of AStar for Part 3**
            - tile_weight?: one of `True` or `False`
                - This will run the modified A* Search with either a weighted greedy heuristic (`True`) or an unweighted greedy heuristic (`False`)
2. Output from Modified A* Search:
    1. Moves
        1. The exact moves necessary to solve the board state
    2. Nodes Expanded
        1. The total number of nodes expanded during the search for the goal
    3. Moves Required
        1. The total number of moves required to reach the goal
    4. Solution Cost
        1. The total cost of the moves adjusted for the tile weights
    5. Estimated Branching Factor
        1. The average number of branches from a parent node to a child node during the search. This is computed with the formula (total # of expanded nodes) ^ (1 / solution node depth)
-------------------------------------------------------------------------------------------------------------------------------------
