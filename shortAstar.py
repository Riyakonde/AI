import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))

    visited = set()
    g_score = {start: 0}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)

        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                tentative_g = g + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor, path + [neighbor]))

    return None

# ----------------------------
# Hardcoded Grid and Positions
# ----------------------------
grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]

start = (0, 0)
goal = (3, 3)

# ----------------------------
# Execution
# ----------------------------
if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
    print("Start or goal position is on an obstacle. No path possible.")
else:
    path = a_star(grid, start, goal)
    print("Shortest Path:", path if path else "No path found.")
