# Map Coloring using CSP

# Define the map as adjacency list
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  []  # Tasmania has no neighbors
}

# Possible colors
colors = ['Red', 'Green', 'Blue']

# Dictionary to store the assigned color for each region
assignment = {}

# Check if the color can be assigned to a region
def is_valid(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking CSP solver
def csp_map_coloring(region_list):
    if not region_list:  # All regions assigned
        return True
    
    region = region_list[0]
    for color in colors:
        if is_valid(region, color):
            assignment[region] = color
            if csp_map_coloring(region_list[1:]):
                return True
            assignment.pop(region)  # Backtrack
    return False

# Solve
if csp_map_coloring(list(neighbors.keys())):
    print("Solution Found:")
    for region in assignment:
        print(f"{region}: {assignment[region]}")
else:
    print("No solution exists.")
