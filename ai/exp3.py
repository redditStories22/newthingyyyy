import heapq
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = float('inf')  # Cost from start to this node
        self.h = 0  # Heuristic cost from this node to the goal
        self.f = float('inf')  # Total cost
    
    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end, allow_diagonal=False):
    open_list = []
    open_dict = {}  # Dictionary for fast lookup
    closed_set = set()
    
    start_node = Node(start)
    start_node.g = 0
    start_node.h = heuristic(start, end)
    start_node.f = start_node.h
    
    heapq.heappush(open_list, start_node)
    open_dict[start] = start_node
    
    move_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if allow_diagonal:
        move_offsets += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    while open_list:
        current_node = heapq.heappop(open_list)
        del open_dict[current_node.position]
        
        if current_node.position == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path
        
        closed_set.add(current_node.position)
        
        for dx, dy in move_offsets:
            neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)
            
            if (neighbor_pos[0] < 0 or neighbor_pos[0] >= len(grid) or
                neighbor_pos[1] < 0 or neighbor_pos[1] >= len(grid[0]) or
                grid[neighbor_pos[0]][neighbor_pos[1]] == 1 or  # Obstacle
                neighbor_pos in closed_set):
                continue
            
            step_cost = 1.4 if allow_diagonal and dx != 0 and dy != 0 else 1
            new_g = current_node.g + step_cost
            
            if neighbor_pos in open_dict and open_dict[neighbor_pos].g <= new_g:
                continue
            
            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.g = new_g
            neighbor_node.h = heuristic(neighbor_pos, end)
            neighbor_node.f = neighbor_node.g + neighbor_node.h
            
            heapq.heappush(open_list, neighbor_node)
            open_dict[neighbor_pos] = neighbor_node
    
    return None  # No path found

def visualize(grid, path, start, end):
    grid_np = np.array(grid)
    plt.figure(figsize=(6,6))
    plt.imshow(grid_np, cmap='Greys', origin='upper')
    
    for (x, y) in path:
        plt.scatter(y, x, c='red', marker='o', s=100)
    
    plt.scatter(start[1], start[0], c='green', marker='s', s=200, label='Start')
    plt.scatter(end[1], end[0], c='blue', marker='s', s=200, label='End')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)
path = astar(grid, start, end, allow_diagonal=True)

if path:
    print("Path:", path)
    visualize(grid, path, start, end)
else:
    print("No path found")