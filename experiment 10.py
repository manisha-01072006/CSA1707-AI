import heapq

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)  # 0 is the blank

# Moves: up, down, left, right
MOVES = {
    'UP': -3,
    'DOWN': 3,
    'LEFT': -1,
    'RIGHT': 1
}

def manhattan_distance(state):
    """Calculate the Manhattan distance heuristic."""
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            goal_x, goal_y = (tile - 1) % 3, (tile - 1) // 3
            curr_x, curr_y = i % 3, i // 3
            distance += abs(goal_x - curr_x) + abs(goal_y - curr_y)
    return distance

def get_neighbors(state):
    """Generate possible moves from current state."""
    neighbors = []
    zero_index = state.index(0)
    x, y = zero_index % 3, zero_index // 3

    # Possible moves
    if y > 0:  # UP
        new_state = list(state)
        swap_idx = zero_index - 3
        new_state[zero_index], new_state[swap_idx] = new_state[swap_idx], new_state[zero_index]
        neighbors.append(tuple(new_state))
    if y < 2:  # DOWN
        new_state = list(state)
        swap_idx = zero_index + 3
        new_state[zero_index], new_state[swap_idx] = new_state[swap_idx], new_state[zero_index]
        neighbors.append(tuple(new_state))
    if x > 0:  # LEFT
        new_state = list(state)
        swap_idx = zero_index - 1
        new_state[zero_index], new_state[swap_idx] = new_state[swap_idx], new_state[zero_index]
        neighbors.append(tuple(new_state))
    if x < 2:  # RIGHT
        new_state = list(state)
        swap_idx = zero_index + 1
        new_state[zero_index], new_state[swap_idx] = new_state[swap_idx], new_state[zero_index]
        neighbors.append(tuple(new_state))

    return neighbors

def a_star(start):
    """A* Search for solving 8-puzzle."""
    frontier = []
    heapq.heappush(frontier, (manhattan_distance(start), 0, start, []))
    explored = set()

    while frontier:
        f, g, state, path = heapq.heappop(frontier)
        if state == GOAL:
            return path

        if state in explored:
            continue
        explored.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in explored:
                new_g = g + 1
                new_f = new_g + manhattan_distance(neighbor)
                heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return None

# Example usage
if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    print("Initial State:")
    for i in range(0, 9, 3):
        print(start_state[i:i+3])

    solution = a_star(start_state)
    if solution:
        print("\nSolution steps:")
        for step in solution:
            for i in range(0, 9, 3):
                print(step[i:i+3])
            print()
        print(f"Total moves: {len(solution)}")
    else:
        print("No solution found.")
