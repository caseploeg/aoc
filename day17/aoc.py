#!/usr/bin/env python3

import sys
from functools import lru_cache
sys.setrecursionlimit(4000)
grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))
    grid[-1] = [int(x) for x in grid[-1]]
start = (0,0)
end = (len(grid)-1, len(grid[0])-1)
import heapq
from collections import defaultdict
dist = dict() 
dist[(0,0,0,1,1)] = 0
dist[(0,0,1,0,1)] = 0
def dp(i,j, di,dj,cons):
    def valid(x, y, c):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if c > 10:
            return False
        return True
    
    q = [(0, (i,j,di,dj,cons))]

    while q:
        curdist, (i,j,di,dj,cons) = heapq.heappop(q)
        if (i,j,di,dj,cons) in dist and  curdist > dist[(i,j,di,dj,cons)]:
            continue
    
        for delta in [(1,0),(-1,0),(0,1),(0,-1)]:
            ddi,ddj = delta
            ccons = cons + 1 if (di, dj) == (ddi, ddj) else 1
            if ccons == 1 and cons < 4:
                continue
            if valid(i+ddi, j+ddj, ccons):
                distance = curdist + grid[i+ddi][j+ddj]
                if (i+ddi,j+ddj,ddi,ddj,ccons) not in dist or distance < dist[(i+ddi, j+ddj, ddi, ddj, ccons)]:
                    dist[(i+ddi, j+ddj, ddi, ddj, ccons)] = distance 
                    heapq.heappush(q, (distance, (i+ddi,j+ddj,ddi,ddj,ccons)))
    return dist
dist = dp(0, 0, 0,1, 1)
for k,v in dist.items():
    (i,j,di,dj,cons) = k
    if i == end[0] and j == end[1]:
        print(v, i, j, di, dj, cons)



        
    








