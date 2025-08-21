import math
import random

def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def check_winner(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def minimax(board, depth, maximizing_player, alpha, beta):
    if check_winner(board, 'X'):
        return -10 + depth, None
    if check_winner(board, 'O'):
        return 10 - depth, None
    if not available_moves(board):
        return 0, None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for move in available_moves(board):
            board[move] = 'O'
            evaluation, _ = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for move in available_moves(board):
            board[move] = 'X'
            evaluation, _ = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_eval, best_move

def computer_move(board):
    _, best_move = minimax(board, 0, True, -math.inf, math.inf)
    return best_move

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move not in available_moves(board):
                print("Invalid move. Try again.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    x=input("Do you want to begin (y/n):")
    if(x=='y' or x=='Y'):
        turn = 'X'
    else:
        turn='O'

    while True:
        if turn == 'X':
            move = player_move(board)
        else:
            print("Computer is thinking...")
            move = computer_move(board)
        board[move] = turn
        print_board(board)

        if check_winner(board, turn):
            print(f"{turn} wins!")
            break
        if not available_moves(board):
            print("It's a draw!")
            break

        turn = 'O' if turn == 'X' else 'X'

if __name__ == "__main__":
    play_game()
