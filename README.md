# AI Maze Solver with Visualization 🤖

This project is a visual implementation of three foundational AI search algorithms: **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **A\* Search**. It generates a random maze and then solves it in real-time, allowing users to see how each algorithm works.

### Key Features

* **Algorithm Visualization:** Watch as the search algorithms explore the maze step-by-step.
* **Multiple Solvers:** Compare the performance of BFS, DFS, and A\* on the same maze.
* **Random Maze Generation:** The project generates a new, solvable maze every time you run it.
* **Command-Line & GUI Output:** View the solved path both in the graphical window and in your terminal. 

### How It Works

Briefly explains the core concepts behind each algorithm.

#### **Breadth-First Search (BFS)**

BFS explores the maze one layer at a time. It's guaranteed to find the **shortest path** because it checks every neighbor at the current distance before moving to the next level.

#### **Depth-First Search (DFS)**

DFS dives as deep as possible down one path before backtracking. It's less efficient for finding the shortest path, but it can be more memory-efficient on very large graphs.

#### **A\* (A-Star) Search**

A\* is an "informed" search algorithm. It's similar to BFS but uses a **heuristic** (estimated distance to the goal) to prioritize which cells to explore. This makes it much faster than BFS while still guaranteeing the shortest path.

### Installation and Usage

Provides clear instructions for someone to run your project.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Mohanakaru/AI-Maze-Solver.git]
    cd AI-Maze-Solver
    ```

2.  **Install the requirements:**
    ```bash
    pip install pygame
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```

4.  **Controls:**
    * Press `1` to solve with BFS.
    * Press `2` to solve with DFS.
    * Press `3` to solve with A\*.
    * Press `SPACE` to generate a new maze.

### Technologies Used

* **Python**: The core programming language.
* **Pygame**: For the graphical user interface and visualization.
