def create_puzzle():
    puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return puzzle

def print_puzzle(puzzle):
    for row in puzzle:
        print(row)

def move_tile(puzzle, direction):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                x, y = i, j

    if direction == "up":
        if x > 0:
            puzzle[x][y], puzzle[x-1][y] = puzzle[x-1][y], puzzle[x][y]
    elif direction == "down":
        if x < 2:
            puzzle[x][y], puzzle[x+1][y] = puzzle[x+1][y], puzzle[x][y]
    elif direction == "left":
        if y > 0:
            puzzle[x][y], puzzle[x][y-1] = puzzle[x][y-1], puzzle[x][y]
    elif direction == "right":
        if y < 2:
            puzzle[x][y], puzzle[x][y+1] = puzzle[x][y+1], puzzle[x][y]
    return puzzle

if _name_ == "_main_":
    puzzle = create_puzzle()
    print_puzzle(puzzle)

    while True:
        direction = input("Enter the direction you want to move the blank tile (up, down, left, right): ")
        puzzle = move_tile(puzzle, direction)
        print_puzzle(puzzle)
