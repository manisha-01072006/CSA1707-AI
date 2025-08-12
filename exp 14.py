from collections import deque

# State: (missionaries_left, cannibals_left, boat_position)
# boat_position: 1 = left bank, 0 = right bank
# Right bank missionaries = 3 - missionaries_left
# Right bank cannibals = 3 - cannibals_left

def is_valid(m_left, c_left):
    """Check if the state is valid (no side has more cannibals than missionaries)."""
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    return True

def bfs():
    start = (3, 3, 1)  # 3 missionaries, 3 cannibals, boat on left
    goal = (0, 0, 0)   # All moved to right

    queue = deque([(start, [])])
    visited = set([start])

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # possible boat trips

    while queue:
        (m_left, c_left, boat), path = queue.popleft()

        if (m_left, c_left, boat) == goal:
            return path + [goal]

        for m, c in moves:
            if boat == 1:  # Boat on left side → move to right
                new_state = (m_left - m, c_left - c, 0)
            else:  # Boat on right side → move to left
                new_state = (m_left + m, c_left + c, 1)

            if is_valid(*new_state[:2]) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [(m_left, c_left, boat)]))

    return None

if __name__ == "__main__":
    solution = bfs()
    if solution:
        print("Missionaries and Cannibals Solution Path:")
        for state in solution:
            m_left, c_left, boat = state
            m_right = 3 - m_left
            c_right = 3 - c_left
            boat_side = "Left" if boat == 1 else "Right"
            print(f"Left: M={m_left}, C={c_left} | Right: M={m_right}, C={c_right} | Boat: {boat_side}")
    else:
        print("No solution found.")
