# Tic Tac Toe Game in Python

# Initialize board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print('| ' + ' | '.join(row) + ' |')
        if i < 2:
            print('-------------')

# Check if a player has won
def check_winner(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

# Check if board is full
def is_full():
    return ' ' not in board

# Main game loop
def tic_tac_toe():
    current_player = 'X'
    while True:
        print_board()
        move = input(f"Player {current_player}, enter your move (1-9): ")
        
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid move. Try again.")
            continue

        move = int(move) - 1
        if board[move] != ' ':
            print("Spot already taken. Try again.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break

        if is_full():
            print_board()
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()
