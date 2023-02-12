def display_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


def check_win(board, player):
    win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                     [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in win_positions:
        if board[i[0]] == board[i[1]] == board[i[2]] == player:
            return True
    return False


def check_draw(board):
    return '-' not in board


board = ['-' for _ in range(9)]
player = 'X'

while True:
    display_board(board)
    print(f"Player {player}, select a position (1-9):")
    pos = int(input()) - 1
    if board[pos] == '-':
        board[pos] = player
        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        player = 'O' if player == 'X' else 'X'
    else:
        print("Invalid position, try again")
