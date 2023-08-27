import queue
import heapq

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

# Define possible moves (up, down, left, right)
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
move_names = ['Right', 'Left', 'Down', 'Up']

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
    
    return None

if __name__ == "__main__":
    maze_file = "maze.txt"
    maze = read_maze(maze_file)
    
    start, goal = find_start_and_goal(maze)
    
    # BFS
    bfs_path = bfs(maze, start, goal)
    if bfs_path:
        print("BFS Path:", bfs_path)
    else:
        print("BFS Path not found.")
    
    # DFS
    dfs_path = dfs(maze, start, goal)
    if dfs_path:
        print("DFS Path:", dfs_path)
    else:
        print("DFS Path not found.")
    
    # UCS
    ucs_path = ucs(maze, start, goal)
    if ucs_path:
        print("UCS Path:", ucs_path)
    else:
        print("UCS Path not found.")
