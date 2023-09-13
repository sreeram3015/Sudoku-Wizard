# Sudoku Solver

This Python program solves Sudoku puzzles using a backtracking algorithm. Sudoku is a popular number puzzle where the objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids that compose the grid contain all of the digits from 1 to 9 without repetition.

## Usage

1. Define the Sudoku grid as a 9x9 2D list in the `sudoku_grid` variable at the beginning of the code. Use `0` to represent empty cells.

2. Run the program.

3. The program will print the initial Sudoku puzzle and then attempt to solve it using a backtracking algorithm.

4. Once solved, the program will display the solution.

## Functions

### `solve_sudoku(s_grid)`

This function takes the Sudoku grid as input and recursively attempts to solve it using a backtracking algorithm. It finds empty cells, tries different numbers, and backtracks if a solution is not found.

### `print_sudoku_grid(s_grid)`

This function prints the Sudoku grid for visual representation. It formats the grid to display it in a readable format.

### `locate_empty_cells(s_grid)`

This function locates and returns the coordinates of empty cells (cells with a value of `0`) in the Sudoku grid.

### `check_validity(s_grid, num, pos)`

This function checks the validity of inserting a number `num` into a given position `pos` in the Sudoku grid. It checks if the number violates the rules of Sudoku in the same row, column, or 3x3 subgrid.

## Note

Make sure to define your Sudoku puzzle in the `sudoku_grid` variable before running the program. Use `0` to represent empty cells in the grid.

Feel free to use, modify, and distribute this code for solving Sudoku puzzles.