import random

def generate_maze(rows, cols):
    # Ensure dimensions are odd for proper maze generation
    if rows % 2 == 0:
        rows += 1
    if cols % 2 == 0:
        cols += 1

    # Initialize grid with walls (1)
    grid = [[1 for _ in range(cols)] for _ in range(rows)]
    
    # Use a list to store active cells
    active_cells = []
    
    # Choose a random starting cell and make it a path (0)
    start_cell = (1, 1)
    grid[start_cell[0]][start_cell[1]] = 0
    active_cells.append(start_cell)

    while active_cells:
        # Pick the most recently added cell
        current_cell = active_cells[-1]
        r, c = current_cell
        
        # Get unvisited neighbors
        unvisited_neighbors = []
        for dr, dc in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
            nr, nc = r + dr, c + dc
            if 0 < nr < rows - 1 and 0 < nc < cols - 1 and grid[nr][nc] == 1:
                unvisited_neighbors.append((nr, nc))

        if unvisited_neighbors:
            # Choose a random neighbor
            next_cell = random.choice(unvisited_neighbors)
            nx, ny = next_cell
            
            # Carve a path by removing the wall between the current and next cell
            grid[(r + nx) // 2][(c + ny) // 2] = 0
            grid[nx][ny] = 0
            active_cells.append(next_cell)
        else:
            # Backtrack
            active_cells.pop()
    
    # Place start and end points after carving the entire maze
    # This guarantees they are on a traversable path.
    grid[1][1] = 'S'
    grid[rows - 2][cols - 2] = 'E'
    
    return grid