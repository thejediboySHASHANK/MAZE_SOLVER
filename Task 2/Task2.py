import queue
import heapq
import time
import random
import matplotlib.pyplot as plt

# Define possible moves (up, down, left, right)
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to generate a maze of a given size with a specified number of empty cells
def generate_maze(size, num_empty_cells):
    maze = [['#' for _ in range(size)] for _ in range(size)]
    
    # Place start (S) and goal (G)
    maze[0][0] = 'S'
    maze[size - 1][size - 1] = 'G'
    
    # Randomly place empty cells (*)
    empty_cells_placed = 0
    while empty_cells_placed < num_empty_cells:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if maze[x][y] == '#':
            maze[x][y] = '*'
            empty_cells_placed += 1
    
    return maze

# Read the maze from a text file and return it as a 2D list
def read_maze(file_path):
    maze = []
    with open(file_path, 'r') as file:
        for line in file:
            maze.append(list(line.strip()))
    return maze

# Function to find the start and goal positions in the maze
def find_start_and_goal(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goal = (i, j)
    return start, goal

# BFS algorithm to find a path from S to G
def bfs(maze, start, goal):
    queue = [(start, [])]
    visited = set()
    
    while queue:
        (x, y), path = queue.pop(0)
        visited.add((x, y))
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                    maze[new_x][new_y] != '#' and (new_x, new_y) not in visited):
                new_path = path + [move_names[moves.index((dx, dy))]]
                if (new_x, new_y) == goal:
                    return new_path
                queue.append(((new_x, new_y), new_path))
    
    return None

# DFS algorithm to find a path from S to G
def dfs(maze, start, goal):
    stack = [(start, [])]
    visited = set()
    
    while stack:
        (x, y), path = stack.pop()
        visited.add((x, y))
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                    maze[new_x][new_y] != '#' and (new_x, new_y) not in visited):
                new_path = path + [move_names[moves.index((dx, dy))]]
                if (new_x, new_y) == goal:
                    return new_path
                stack.append(((new_x, new_y), new_path))
    
    return None

# UCS algorithm to find a path from S to G
def ucs(maze, start, goal):
    heap = [(0, start, [])]
    visited = set()
    
    while heap:
        cost, (x, y), path = heapq.heappop(heap)
        visited.add((x, y))
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                    maze[new_x][new_y] != '#' and (new_x, new_y) not in visited):
                new_cost = cost + 1  # Uniform cost
                new_path = path + [move_names[moves.index((dx, dy))]]
                if (new_x, new_y) == goal:
                    return new_path
                heapq.heappush(heap, (new_cost, (new_x, new_y), new_path))

# Measure the running time for an algorithm on a given maze
def measure_running_time(algorithm, maze, start, goal):
    start_time = time.time()
    algorithm(maze, start, goal)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    maze_sizes = [20, 50, 100, 500, 1000]
    num_empty_cells = [10, 25, 50, 250, 500]  # Corresponding number of empty cells for each maze size
    
    bfs_times = []
    dfs_times = []
    ucs_times = []
    
    for size, empty_cells in zip(maze_sizes, num_empty_cells):
        maze = generate_maze(size, empty_cells)
        start, goal = find_start_and_goal(maze)
        
        bfs_time = measure_running_time(bfs, maze, start, goal)
        dfs_time = measure_running_time(dfs, maze, start, goal)
        ucs_time = measure_running_time(ucs, maze, start, goal)
        
        bfs_times.append(bfs_time)
        dfs_times.append(dfs_time)
        ucs_times.append(ucs_time)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(maze_sizes, bfs_times, marker='o', label='BFS')
    plt.plot(maze_sizes, dfs_times, marker='o', label='DFS')
    plt.plot(maze_sizes, ucs_times, marker='o', label='UCS')
    plt.xlabel('Maze Size')
    plt.ylabel('Running Time (s)')
    plt.title('Maze Size vs. Running Time for Search Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()
