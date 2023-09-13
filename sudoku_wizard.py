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
    for i in range(len(s_grid)):
        if i%3 == 0 and i !=0:
            print("- - - - - - - - - - - - ")
        
        for j in range(9):
            if j%3 ==0 and j!=0:
                print(" | ", end="")

            if j==8:
                print(s_grid[i][j])
            else:
                print(str(s_grid[i][j]) + " ", end="")
    print("")

print_sudoku_grid(sudoku_grid)
