# Define the Sudoku grid as a 2D list
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Function to solve the Sudoku grid using a backtracking algorithm
def solve_sudoku(s_grid):
    # Find empty cells in the grid
    empty_cells = locate_empty_cells(s_grid)
    # If no empty cells remain, the Sudoku is solved
    if not empty_cells:
        return True

    for row, column in empty_cells:
        for num in range(1, 10):
            # Check if the current number is valid in the current position
            if check_validity(s_grid, num, (row, column)):
                s_grid[row][column] = num

                # Recursively attempt to solve the Sudoku
                if solve_sudoku(s_grid):
                    return True

                # If the current configuration is invalid, reset the cell
                s_grid[row][column] = 0

        # If no valid number is found for the current cell, backtrack
        return False
    
    # Handle the case where the grid is already filled
    return True

# Function to print the Sudoku grid for visual representation
def print_sudoku_grid(s_grid):
    print("")
    for r in range(len(s_grid)):
        if r % 3 == 0 and r != 0:
            print("- - - - - - - - - - - - ")

        for c in range(len(s_grid[0])):
            if c % 3 == 0 and c != 0:
                print(" | ", end="")

            if c == 8:
                print(s_grid[r][c])
            else:
                print(str(s_grid[r][c]) + " ", end="")
    print("")

# Function to locate and return the coordinates of empty cells
def locate_empty_cells(s_grid):
    empty_cells = []
    for r in range(len(s_grid)):        # Iterate through rows
        for c in range(len(s_grid[0])):  # Iterate through columns
            if s_grid[r][c] == 0:
                empty_cells.append((r, c))
    return empty_cells

# Function to check the validity of inserting a number into a given position
def check_validity(s_grid, num, pos):
    # Check row
    for r in range(len(s_grid[0])):
        if s_grid[pos[0]][r] == num and pos[1] != r:
            return False

    # Check column
    for c in range(len(s_grid)):
        if s_grid[c][pos[1]] == num and pos[0] != c:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if s_grid[i][j] == num and (i, j) != pos:
                return False
    
    return True

# Display the initial Sudoku puzzle
print("Question: ")
print_sudoku_grid(sudoku_grid)
print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")

# Solve the Sudoku puzzle
solve_sudoku(sudoku_grid)

# Display the solved Sudoku puzzle
print("Solution: ")
print_sudoku_grid(sudoku_grid)
