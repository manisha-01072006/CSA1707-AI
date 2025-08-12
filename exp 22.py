# Minimax Algorithm for Tic-Tac-Toe

import math

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
    print()

# Function to check for a winner
def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Function to check if board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Minimax function
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":  # AI win
        return 1
    elif winner == "X":  # Human win
        return -1
    elif is_full(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Function to get the AI's best move
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
board = [[" " for _ in range(3)] for _ in range(3)]

while True:
    print_board(board)
    if check_winner(board) or is_full(board):
        break

    # Player move
    x, y = map(int, input("Enter your move (row col): ").split())
    if board[x][y] != " ":
        print("Invalid move, try again.")
        continue
    board[x][y] = "X"

    if check_winner(board) or is_full(board):
        break

    # AI move
    ai_move = best_move(board)
    if ai_move:
        board[ai_move[0]][ai_move[1]] = "O"

print_board(board)
winner = check_winner(board)
if winner:
    print("Winner:", winner)
else:
    print("It's a draw!")
