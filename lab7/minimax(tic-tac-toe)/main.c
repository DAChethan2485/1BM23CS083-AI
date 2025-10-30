import math

HUMAN = 'O'
AI = 'X'
EMPTY = ' '

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)
    print()

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def minimax(board, depth, alpha, beta, maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    elif winner == HUMAN:
        return depth - 10
    elif is_full(board):
        return 0

    if maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        return max_eval
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        return min_eval
        return min_eval

def best_move(board):
    best_val = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def play():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe (You are O, AI is X)\n")
    print_board(board)
    while True:
        row = int(input("Enter your row (0-2): "))
        col = int(input("Enter your column (0-2): "))
        if board[row][col] != EMPTY:
            print("Cell already taken! Try again.")
            continue
        board[row][col] = HUMAN
        print_board(board)
        if check_winner(board) == HUMAN:
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        print("AI is thinking...")
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = AI
        print_board(board)
        if check_winner(board) == AI:
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play()
