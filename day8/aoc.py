#!/usr/bin/env python3

import sys

rl = sys.stdin.readline().strip()
sys.stdin.readline()
adj_graph = dict() 
for line in sys.stdin:
    node, adj = line.split(' = ')
    adj = adj.strip().strip('())').split(', ')
    adj_graph[node] = adj
    



count = 0
start = []
for node in adj_graph:
    if node[-1] == 'A':
        start.append(node)

# print(adj_graph)
for j in range(len(start)):
    cycles = dict()
    flag = False
    node = start[j]
    count =0
    while flag == False:
        for i, c in enumerate(rl):
            if c == 'L':
                node = adj_graph[node][0]
            else:
                node = adj_graph[node][1]   
            count += 1
            if node[-1] == 'Z':
                if (node, i) not in cycles:
                    cycles[(node, i)] = count
        if count > 200_000:
            break 
    print(cycles)


# pick the smallest p st. p % a == 0 for all a 

        
                