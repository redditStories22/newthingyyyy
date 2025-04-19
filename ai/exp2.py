import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


network = nx.Graph()
network.add_edges_from([
    ("A", "B"), ("B", "C"), ("C", "D"), 
    ("D", "E"), ("E", "F"), ("F", "G"), 
    ("G", "H"), ("A", "D"), ("F", "C")
])

def bfs(graph, start, end):
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        
        for neigh in graph.neighbors(node):
            if neigh not in path:
                queue.append(path + [neigh])
    return None

def dfs(graph, start, end, path=None):
    if path is None:
        path = [start]
    
    if start == end:
        return path
    
    for neigh in graph.neighbors(start):
        if neigh not in path:
            new_path = dfs(graph, neigh, end, path + [neigh])
            if new_path:
                return new_path
    return None

start = "A"
end = "H"
print("BFS TRAVEL:", bfs(network, start, end))
print("DFS TRAVEL:", dfs(network, start, end))

plt.figure(figsize=(8, 5))
pos = nx.spring_layout(network)
nx.draw(network, pos, with_labels=True)
plt.show()