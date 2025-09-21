import pygame
import time
from algorithm import bfs, dfs, a_star
from generator import generate_maze

# --- Constants for Pygame ---
WIDTH, HEIGHT = 600, 600
TILE_SIZE = 20
ROWS = WIDTH // TILE_SIZE
COLS = HEIGHT // TILE_SIZE
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Maze Solver")

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
TEAL = (0, 128, 128)

def print_maze_to_terminal(maze, path):
    """
    Prints the maze with the solved path to the terminal.
    """
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if (r, c) in path and cell != 'S' and cell != 'E':
                print('*', end=' ')
            else:
                print(cell, end=' ')
        print()
    print("\n" + "="*40 + "\n")

def draw_grid(maze):
    for r in range(ROWS):
        for c in range(COLS):
            color = WHITE
            if maze[r][c] == 1:
                color = BLACK
            elif maze[r][c] == 'S':
                color = GREEN
            elif maze[r][c] == 'E':
                color = RED
            
            pygame.draw.rect(WIN, color, (c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    pygame.display.update()

def draw_path(path):
    for r, c in path:
        rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(WIN, YELLOW, rect, 2)
    pygame.display.update()

def draw_visited(visited_nodes, path_color):
    for r, c in visited_nodes:
        rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(WIN, path_color, rect)
    pygame.display.update()

def find_start_end(maze):
    start, end = None, None
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
            elif cell == 'E':
                end = (r, c)
    return start, end

def run_solver(algorithm_name, algorithm, maze):
    start, end = find_start_end(maze)
    if not start or not end:
        print("Start or end point not found.")
        return None

    print(f"Solving with {algorithm_name}...")
    
    solution_generator = algorithm(maze, start, end)
    solved = False
    final_path = None
    
    while not solved:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        try:
            explored_nodes = next(solution_generator)
            draw_grid(maze)
            draw_visited(explored_nodes, TEAL)
            pygame.display.flip()
            time.sleep(0.01)
        except StopIteration as e:
            final_path = e.value
            if final_path:
                draw_path(final_path)
            else:
                print("No path found.")
            solved = True

    time.sleep(2)
    return final_path

def main():
    maze = generate_maze(ROWS, COLS)
    draw_grid(maze)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    path = run_solver("BFS", bfs, maze)
                    if path:
                        print_maze_to_terminal(maze, path)
                elif event.key == pygame.K_2:
                    path = run_solver("DFS", dfs, maze)
                    if path:
                        print_maze_to_terminal(maze, path)
                elif event.key == pygame.K_3:
                    path = run_solver("A*", a_star, maze)
                    if path:
                        print_maze_to_terminal(maze, path)
                elif event.key == pygame.K_SPACE:
                    maze = generate_maze(ROWS, COLS)
                    draw_grid(maze)
                    print("New maze generated. Press 1, 2, or 3 to solve.")
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()