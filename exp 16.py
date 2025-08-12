from collections import deque

def bfs(graph, start):
    visited = set()  # Track visited nodes
    queue = deque([start])  # Initialize queue with start node
    
    while queue:
        node = queue.popleft()  # Get next node from queue
        
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)
            
            # Add all unvisited neighbors to queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS
print("BFS Traversal starting from node A:")
bfs(graph, 'A')
