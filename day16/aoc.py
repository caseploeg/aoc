#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4000)
seen = set()
def next(i,j,di,dj):
    if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
        return
    if (i,j,di,dj) in seen:
        return
    seen.add((i,j,di,dj))
    #print(i,j,grid[i][j])
    #print('\n'.join((''.join(x) for x in energy)) )
    energy[i][j] = '#'
    if grid[i][j] == '.':
        next(i+di,j+dj, di, dj)
    elif grid[i][j] == '|':
        if dj != 0:
            next(i+1,j,1,0)
            next(i-1,j,-1,0)
        else:
            next(i+di,j+dj,di,dj)
    elif grid[i][j] == '-':
        if di != 0:
            next(i,j-1,0,-1)
            next(i,j+1,0,1)
        else:
            next(i+di,j+dj,di,dj)
    elif grid[i][j] == '\\':
            di, dj = dj, di
            next(i+di,j+dj,di,dj)
    elif grid[i][j] == '/':
            di, dj = -dj, -di
            next(i+di,j+dj,di,dj)


energy = []
grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))
    energy.append(['.' for _ in range(len(grid[0]))])

e = '\n'.join((''.join(x) for x in energy))

t = 0

coords = []
for i in range(len(grid)):
    coords.append((i,0))
    coords.append((i,len(grid[0])-1))

for j in range(len(grid)):
    coords.append((0,j))
    coords.append((len(grid)-1,j))

for (i,j) in coords:
    energy = [list(_) for _ in e.split('\n')]
    seen = set()
    next(i,j,0,1)
    energy = '\n'.join((''.join(x) for x in energy))
    total = 0
    for c in energy:  
        if c == '#':
            total += 1
    t = max(t, total)

print(t)