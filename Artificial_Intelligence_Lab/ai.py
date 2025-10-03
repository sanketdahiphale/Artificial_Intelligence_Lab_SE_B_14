from queue import PriorityQueue

# Graph representation
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'D': 12},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 7},
    'D': {'G': 2},
    'G': {}
}

# Heuristic values
heuristics = {
    'S': 7, 'A': 6, 'B': 4,
    'C': 2, 'D': 1, 'G': 0
}

def a_star_search(start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0

    while not open_list.empty():
        _, current = open_list.get()

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path)), g_scores[goal]

        for neighbor, cost in graph[current].items():
            tentative_g = g_scores[current] + cost
            if tentative_g < g_scores[neighbor]:
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristics[neighbor]
                open_list.put((f_score, neighbor))
    
    return None, float('inf')

# Run A*
path, cost = a_star_search('S', 'G')
print("Path:", path)
print("Total Cost:", cost)

