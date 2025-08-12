N = 8  # Board size

def print_board(board):
    """Print the chess board."""
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col]."""
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False

    return True

def solve(board, row):
    """Recursive backtracking to place queens."""
    if row == N:  # All queens placed
        print_board(board)
        return True

    found_solution = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            found_solution = solve(board, row + 1) or found_solution
            board[row][col] = 0  # Backtrack

    return found_solution

if __name__ == "__main__":
    board = [[0] * N for _ in range(N)]
    if not solve(board, 0):
        print("No solution found.")
