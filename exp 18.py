from itertools import permutations

# Travelling Salesman Problem using brute-force
def travelling_salesman(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = float("inf")
    best_route = []

    # Generate all possible routes
    for perm in permutations(vertices):
        current_cost = 0
        current_path = [start] + list(perm) + [start]

        # Calculate cost of this route
        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i + 1]]

        # Update if found shorter path
        if current_cost < min_path:
            min_path = current_cost
            best_route = current_path

    return best_route, min_path


# Example graph (distance matrix as dictionary of dictionaries)
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

# Run TSP
route, cost = travelling_salesman(graph, 'A')
print("Best Route:", " -> ".join(route))
print("Minimum Cost:", cost)
