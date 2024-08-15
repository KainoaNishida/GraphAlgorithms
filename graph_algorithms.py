# explanations for these functions are provided in requirements.py

from graph import Graph

def get_diameter(graph: Graph) -> int:
    random_node = graph.get_random_node()
    max_distance = 0
    farthest_node = random_node

    for _ in range(20):
        distance, farthest_node = bfs(graph, farthest_node)
        if distance > max_distance:
            max_distance = distance

    return max_distance

def get_degree_distribution(graph: Graph) -> dict[int, int]:
    degree = {}
    keys = set()
    for vertex in range(graph.get_num_nodes()):
        degree[vertex] = len(graph.get_neighbors(vertex))
          
    histogram = {}
    for key, value in degree.items():
          if value in keys:
              histogram[value] += 1

          else:
              histogram[value] = 1
              keys.add(value)
    
    return histogram

def get_clustering_coefficient(graph: Graph) -> float:
    return (3 * triangle_count(graph)) / number_of_two_edge_paths(graph)


def bfs(graph: Graph, start_node: int) -> tuple:
    # Performs the second heuristic of calculating diameter given in class. 
    queue = [(start_node, 0)]
    visited = set([start_node])
    max_node = (0, start_node)

    while queue:
        curr, distance = queue.pop(0)

        if distance > max_node[0]:
            max_node = (distance, curr)

        for neighbor in graph.get_neighbors(curr):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return max_node

def number_of_two_edge_paths(graph: Graph) -> int:
    # Calculates the number of two edge paths in a given graph
    deg = graph.get_degrees()
    rv = 0
    for v in graph.get_nodes():
        rv += deg[v] * (deg[v]-1)/2
    return rv


def triangle_count(graph: Graph):
    # Calculates the number of triangles in a graph
    L, Nv = build_degeneracy(graph)
    triangle_count = 0

    
    for vertex in L:
        if vertex in Nv.keys():
            for u, w in choose_two_permutations(Nv[vertex]):
                if w in graph.get_neighbors(u):
                    triangle_count += 1
            
    return triangle_count


def choose_two_permutations(iterable: set):
    n = len(iterable)
    list_iterable = list(iterable)
    for i in range(n):
        for j in range(i + 1, n):
            yield (list_iterable[i], list_iterable[j])


def build_degeneracy(graph: Graph) -> tuple[list: 'L', dict: 'Nv']:
    L = [] # return value: the degeneracy list of the graph
    remaining_degrees = graph.get_degrees().copy() 
    n = graph.size() 
    D = {} # key = remaining_degree, value = all nodes with that remaining degree
    for key, value in remaining_degrees.items():
        if value not in D.keys():
            D[value] = set()
        D[value].add(key)
    
    
    
    N = {} # key = node, value = all nodes that come before v in L
    H = [False for _ in range(n)] # H[i] = true if vertex i is in L; false otherwise
    k = 0

    for _ in range(n):
        i = 0
        while True:
            if i in D.keys() and D[i] != set():
                break
            i += 1
        
        k = max(k, i)
        v = D[i].pop()
        L.insert(0, v)
        H[v] = True # to reflect the fact that v has been stored in L

        for w in graph.get_neighbors(v):
            if H[w]: # true if w is already in L; false otherwise
                continue

            curr_degree = remaining_degrees[w]
            new_degree = remaining_degrees[w] - 1
            
            remaining_degrees[w] -= 1
            D[curr_degree].remove(w)
            if new_degree not in D.keys():
                D[new_degree] = set()
            
            D[new_degree].add(w)

            if v not in N.keys():
                N[v] = set()
            N[v].add(w)

    return L, N


          


