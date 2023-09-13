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

#function to check the validity
def check_validity(s_grid, num, pos):
    #Check row
    for r in range(9):
        if s_grid[pos[0]][r] == num and pos[1] != r:
            return False

    #Check column
    for c in range(9):
        if s_grid[c][pos[1]] == num and pos[0] != c:
            return False

    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if s_grid[i][j] == num and (i, j) != pos:
                return False
    
    return True