from graph import Graph
from math import log
import random

def erdos_renyi_graph(n):
    p = 2 * log(n) / n
    edges = set()
    v = 0
    w = -1

    while v < n:
        r = random.random()
        w += 1 + int(log(1 - r) / log(1 - p))
        while w >= v and v < n:
            w -= v
            v += 1
        if v < n:
            edges.add((v, w))

    return Graph(n, edges)
