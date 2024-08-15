import numpy as np
from graph import Graph
import random

def barabasi_albert_graph(n, d = 5):
    M = [0] * (2 * n * d)  
    E = set()  

    for v in range(n):
        for i in range(d):
            M[2 * (v * d + i)] = v
            r = random.randint(0, 2 * (v * d + i))
            M[2 * (v * d + i) + 1] = M[r]
    
    for i in range(n * d):
        E.add((M[2 * i], M[2 * i + 1]))

    return Graph(n, E)

# # Example usage
# num_nodes = 100  # Number of nodes
# d = 5  # Number of neighbors each new vertex connects to
# ba_graph = barabasi_albert_graph(num_nodes, d)

# print(f"Barabasi-Albert Graph: {ba_graph.size()} nodes, {ba_graph.get_num_edges()} edges")
