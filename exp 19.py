from queue import PriorityQueue

def a_star_search(graph, heuristic, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g_score[goal]

        for neighbor, cost in graph[current]:
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                open_list.put((f_score, neighbor))

    return None, float("inf")


# Example Graph: adjacency list (node: [(neighbor, cost)])
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values (straight-line estimates to goal 'G')
heuristic = {
    'A': 7, 'B': 6, 'C': 5,
    'D': 3, 'E': 1, 'F': 2, 'G': 0
}

# Run A*
path, cost = a_star_search(graph, heuristic, 'A', 'G')
print("Optimal Path:", " -> ".join(path))
print("Total Cost:", cost)
