import heapq

# Example graph
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

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], 0, start, [start]))
    closed_list = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        closed_list.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in closed_list:
                continue
            new_g = g + cost
            new_f = new_g + heuristics[neighbor]
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

# Run A*
start, goal = 'S', 'G'
path, cost = a_star(start, goal)
print("Path found:", path)
print("Total cost:", cost)

