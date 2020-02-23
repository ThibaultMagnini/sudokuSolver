#solution to sudoku solver Kata (3 Kyu) found on codewars.com


# recursive function that first checks for empty nodes
# if an empty node is found it will check for all numbers
# if a valid number is found the function will call itself so the process is repeated
# until no empty nodes are found 
def solve(puzzle):
    find = find_empty_node(puzzle)
    if not find:
        return True
    else:
        row, col = find

    for n in range(1,10):
        if valid(puzzle, n, (row, col)):
            puzzle[row][col] = n

            if solve(puzzle):
                return True

            puzzle[row][col] = 0

    return False


#checks if a number is a valid option
def valid(puzzle, num, n):
    #checks the row
    for x in range(len(puzzle[0])):
        if puzzle[n[0]][x] == num and n[1] != x:
            return False

    #checks the column 
    for y in range(len(puzzle)):
        if puzzle[y][n[1]] == num and n[0] != y:
            return False

    #checks the 3 by 3 square for validity 
    x0 = n[1] // 3
    y0 = n[0] // 3

    for x in range(y0 * 3, y0 * 3 + 3):
        for y in range(x0 * 3, x0 * 3 + 3):
            if puzzle[x][y] == num and (x,y) != n:
                return False
    return True



#Goes trough the 2d array to check for empty nodes which in this case are set to 0
def find_empty_node(puzzle):
    for x in range(len(puzzle)):
        for y in range(len(puzzle[0])):
            if puzzle[x][y] == 0:
                return (x, y)
    return None


    
def sudoku(puzzle):
    solve(puzzle)
    return puzzle


sudoku([[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]])