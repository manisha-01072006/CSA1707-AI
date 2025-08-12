import random

def vacuum_cleaner_random(rows, cols):
    # Create grid with all rooms dirty
    env = [['Dirty' for _ in range(cols)] for _ in range(rows)]

    # Start position
    pos = (0, 0)
    steps = 0

    # Keep running until all rooms are clean
    while any('Dirty' in row for row in env):
        r, c = pos
        print(f"Step {steps}: Position: {pos}, Environment:")
        for row in env:
            print(row)

        if env[r][c] == 'Dirty':
            print(f" - Cleaning at {pos}")
            env[r][c] = 'Clean'
        else:
            # Move to a random adjacent room
            moves = []
            if r > 0: moves.append((r-1, c))  # up
            if r < rows-1: moves.append((r+1, c))  # down
            if c > 0: moves.append((r, c-1))  # left
            if c < cols-1: moves.append((r, c+1))  # right
            pos = random.choice(moves)
            print(f" - Moving to {pos}")

        steps += 1

    print("\nFinal State:")
    for row in env:
        print(row)
    print(f"All rooms are clean in {steps} steps!")

if __name__ == "__main__":
    vacuum_cleaner_random(2, 3)  # 2x3 grid
