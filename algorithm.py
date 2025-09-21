import heapq
from collections import deque

def reconstruct_path(parent, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

def bfs(maze, start, end):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    explored = []

    while queue:
        current = queue.popleft()
        explored.append(current)
        yield explored # Yield explored nodes for visualization
        
        if current == end:
            return reconstruct_path(parent, end)

        r, c = current
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        for neighbor in neighbors:
            nr, nc = neighbor
            if (0 <= nr < len(maze) and 
                0 <= nc < len(maze[0]) and 
                maze[nr][nc] != 1 and 
                neighbor not in visited):
                
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current
    
    return None

def dfs(maze, start, end):
    stack = [start]
    visited = {start}
    parent = {start: None}
    explored = []

    while stack:
        current = stack.pop()
        explored.append(current)
        yield explored
        
        if current == end:
            return reconstruct_path(parent, end)

        r, c = current
        # Reverse neighbor order for consistent search direction
        neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        for neighbor in neighbors:
            nr, nc = neighbor
            if (0 <= nr < len(maze) and 
                0 <= nc < len(maze[0]) and 
                maze[nr][nc] != 1 and 
                neighbor not in visited):
                
                visited.add(neighbor)
                stack.append(neighbor)
                parent[neighbor] = current
    
    return None

def a_star(maze, start, end):
    open_set = [(0, 0, start)]
    g_costs = {start: 0}
    parent = {start: None}
    explored = []

    while open_set:
        f_cost, g_cost, current = heapq.heappop(open_set)
        explored.append(current)
        yield explored
        
        if current == end:
            return reconstruct_path(parent, end)

        r, c = current
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        for neighbor in neighbors:
            nr, nc = neighbor
            if not (0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != 1):
                continue

            new_g_cost = g_costs.get(current, float('inf')) + 1

            if new_g_cost < g_costs.get(neighbor, float('inf')):
                parent[neighbor] = current
                g_costs[neighbor] = new_g_cost
                
                h_cost = abs(nr - end[0]) + abs(nc - end[1])
                f_cost = new_g_cost + h_cost
                
                heapq.heappush(open_set, (f_cost, new_g_cost, neighbor))
    
    return None