# How to Run the Program

To run the program, follow these steps:

1. Open a terminal.
2. Navigate to the directory containing the code files.
3. Run the program using the following command:

   `python your_chosen_filename.py <algorithm_name>`

Replace `your_chosen_filename.py` with the name of your Python code file, which can be anything you decide (e.g., `8puzzle_solver.py`).

Replace `<algorithm_name>` with one of the following values:

- `dfs`: For running the Depth-first search algorithm
- `ids`: For running the Iterative deepening search algorithm
- `astar1`: For running the A\* algorithm with heuristic 1.
- `astar2`: For running the A\* algorithm with heuristic 2.

After running the program, enter the initial state of the puzzle when prompted. You can input the numbers directly into the terminal, and **use `0` to represent the empty tile. **

The program will then output the sequence of board positions that solve the puzzle, the total number of moves, and the total number of search states enqueued.

### Sample Input and Corresponding Output

Input:

1 0 2
4 5 3
6 7 8

Output:

[[1 0 2]
 [4 5 3]
 [6 7 8]]
  depth= 0     action= None

[[1 2 0]
 [4 5 3]
 [6 7 8]]
  depth= 1     action= left

[[1 2 3]
 [4 5 0]
 [6 7 8]]
  depth= 2     action= up

[[1 2 3]
 [4 0 5]
 [6 7 8]]
  depth= 3     action= right

Number of moves =  3
Maximum priority queue depth =  3
Number of states enqueued = 12

### Report.pdf

#### Comparative Analysis of Heuristics for A* Algorithm

1. **Misplaced Tiles Heuristic**

   - This heuristic calculates the number of misplaced tiles between the current state and the goal state.
   - It underestimates the actual cost to reach the goal state.
   - While simple to implement, it may not always be very accurate, especially in more complex puzzles where rearranging tiles might require several moves.
2. **Manhattan Distance Heuristic**

   - This heuristic calculates the sum of the Manhattan distances of each tile from its goal position.
   - It provides a better estimation of the cost to reach the goal state compared to the misplaced tiles heuristic.
   - The Manhattan distance represents the minimum number of moves required to move each tile to its correct position.
   - While more complex to implement, it usually yields better results and can handle a wider range of puzzle configurations effectively.

In conclusion, while both heuristics can be used for the A* algorithm, the Manhattan distance heuristic generally provides better performance and accuracy, especially for more complex puzzles. However, it comes with the cost of increased computational complexity. Therefore, the choice of heuristic depends on the specific requirements and constraints of the problem at hand.
