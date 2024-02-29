#!/usr/bin/env python3

from functools import lru_cache
im1 = 93366
im2 = 33680
for _ in range(202300-2):
    cur = 2*im1 - im2 + 29790 
    im2 = im1
    im1 = cur
print(cur)
exit()





import sys
grid = []
lines = []
expand =10 
for line in sys.stdin:
    lines.append(line.strip()*expand)
for i in range(expand):
    for line in lines:
        grid.append(list(line))

l = len(grid)
w = len(grid[0])
print(l,w)
counts = []
scount = 0
for i in range(l):
    for j in range(w):
        #print(i,j)
        if grid[i][j] == 'S':
            scount += 1
            mid = (((expand // 2) + 1)*expand
            + expand // 2)
            if scount == mid:
                si, sj = i,j
                grid[i][j] = 'O'
            else:
                grid[i][j] = '.'


# shortest path from S to x
# = S to y + y to x
# shortest path across 2 grids

#f(i) = f(i-1)-f(i-2) + 162 + f(i-1)
#f(i) = (2*f(i-1))-f(i-2) + 162


steps = 600 
deltas = [(1,0),(-1,0),(0,1),(0,-1)]
#deltas = [(1,0),(0,1)]
count = 0
from collections import defaultdict
highseen = defaultdict(list)
for _ in range(steps):
    high = 0
    for i in range(l):
        for j in range(w):
            if grid[i][j] == 'O':
                for (di,dj) in deltas:
                    if i + di >= 0 and i + di < l and j + dj >= 0 and j + dj < w:
                        if grid[i+di][j+dj] == '.': 
                            grid[i+di][j+dj] = 'n'
                            high = max(high,i)
    for i in range(l):
        for j in range(w):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
    

    count = 0
    for i in range(l):
        for j in range(w):
            if grid[i][j] == 'n':
                grid[i][j] = 'O'
                count += 1
    counts.append(count)
    highstr = ''.join(grid[high])
    highseen[highstr].append([count, _])

grid[si][sj] = 'S'
for k,v in highseen.items():
    print(v)
    if v[0][1] == 64:
        counts = v
    #print(v)
#print('\n'.join((''.join(x) for x in grid)))
print(counts)

ncounts = [] 
for i in range(len(counts)):
    ncounts.append(counts[i][0])
counts = ncounts
while True:
    ncounts = [] 
    for i in range(1, len(counts)):
        ncounts.append(counts[i] - counts[i-1])
    print(ncounts)
    counts = ncounts
    if len(ncounts) == 1:
        break





print(f1(44))

exit()
print(counts)
 