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

#printing the grid for visual representation
def print_sudoku_grid(s_grid):
    print("")
    for r in range(9):
        if r%3 == 0 and r !=0:
            print("- - - - - - - - - - - - ")
        
        for c in range(9):
            if c%3 ==0 and c!=0:
                print(" | ", end="")

            if c==8:
                print(s_grid[r][c])
            else:
                print(str(s_grid[r][c]) + " ", end="")
    print("")

#function to locate empty shells
def locate_empty_cell(s_grid):
    for r in range(9):      #row
        for c in range(9):  #column
            return(r, c)