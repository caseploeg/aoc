#!/usr/bin/env python3
import sys
edges = set()
from collections import defaultdict
adj = defaultdict(list)
start = ''
for line in sys.stdin:
    node, fam = line.strip().split(': ')
    fam = fam.split(' ')
    start = node
    for n in fam:
        edges.add((node,n))
        edges.add((n,node))
        adj[node].append(n)
        adj[n].append(node)


import itertools
num_nodes = len(adj)
print(num_nodes)
edgecount = defaultdict(int)
t = 0

# connected graph: E >= V - 1
 # ... # ... # ... # ... # .. #
 # find all the shortest paths
 # if some edge is in none of the shortest paths,
 # then removing it will do nothing, remove from consideration for the cut
 # remove the edge that occurs most often in shortest paths, then recalculate
 # do this twice?

import random

def karger_min_cut(graph):
    """
    Karger's algorithm to find the minimum cut of a graph.
    graph: A dictionary representation of the undirected graph where each key is a vertex,
           and its corresponding value is a list of vertices to which it is connected (its edges).
    """
    # Copy the graph to avoid altering the original graph
    local_graph = {u: list(v) for u, v in graph.items()}
    g_size = dict()
    for u in local_graph:
        g_size[u] = 1
    
    # Keep contracting edges until there are only two vertices left
    while len(local_graph) > 2:
        # Select a random edge by first selecting a random vertex
        u = random.choice(list(local_graph.keys()))
        # Then select a vertex it is connected to
        v = random.choice(local_graph[u])
        
        # Contract the edge (u, v)
        # Merge the vertex list of v into u and remove v from the graph
        for vertex in local_graph[v]:
            if vertex != u:  # Avoid self-loops
                local_graph[u].append(vertex)
            local_graph[vertex].remove(v)
            if vertex != u:
                local_graph[vertex].append(u)
        
        # Remove self-loops
        local_graph[u] = [vertex for vertex in local_graph[u] if vertex != u]
        
        # Finally, remove vertex v
        g_size[u] += g_size[v]
        del local_graph[v]
    
    # After the contraction process, there will be two vertices left, each representing a set of the original graph.
    # The number of edges between these two sets is the cut size.
    min_cut = len(local_graph[list(local_graph.keys())[0]])
    for u in local_graph.keys():
        print(g_size[u])
    return min_cut

for _ in range(20):
    mk = karger_min_cut(adj)
    if mk == 3:
        print(mk)
        exit()
    print()
