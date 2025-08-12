from collections import deque

def water_jug_solver(jug1, jug2, target):
    visited = set()  # Keep track of visited states
    q = deque()

    # Each state is (amount in jug1, amount in jug2)
    q.append((0, 0))
    visited.add((0, 0))

    while q:
        x, y = q.popleft()
        print(f"({x}, {y})")  # Current state

        # If we reach the target in either jug
        if x == target or y == target:
            print("\nTarget reached!")
            return True

        # Possible moves
        possible_states = [
            (jug1, y),        # Fill jug1
            (x, jug2),        # Fill jug2
            (0, y),           # Empty jug1
            (x, 0),           # Empty jug2
            # Pour jug1 -> jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),
            # Pour jug2 -> jug1
            (x + min(y, jug1 - x), y - min(y, jug1 - x))
        ]

        for state in possible_states:
            if state not in visited:
                visited.add(state)
                q.append(state)

    print("No solution possible.")
    return False


# Example usage
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_amount = 2

    water_jug_solver(jug1_capacity, jug2_capacity, target_amount)
