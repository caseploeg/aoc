#!/usr/bin/env python3

import sys

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))

empty_row = set()
for i in range(len(grid)):
    flag =True
    for c in grid[i]:
        if c != '.':
            flag = False 
            break
    if flag:
        empty_row.add(i)
# *grid -> expands grid into a list of params
# zip() -> takes an element from each param, making new lists
# zip(*grid) -> converts rows to columns
empty_column = set()
ng = list(zip(*grid))
for i in range(len(ng)):
    flag =True
    for c in ng[i]:
        if c != '.':
            flag = False 
            break
    if flag:
        empty_column.add(i)

count = 0
loc = dict()
for i in range(len(grid)):
    for j in range (len(grid[0])):
        if grid[i][j] == '#':
            grid[i][j] = count
            loc[count] = (i,j) 
            count += 1

print('\n'.join([str(x) for x in grid]))

print(empty_column, empty_row)
from functools import reduce
total = 0
for a in range(count):
    for b in range(count):
        if a < b:
            i, j = loc[a]
            ii, jj = loc[b]
            si,ei = min(i, i), max(i, ii)
            ni = ei
            for x in range(si,ei+1):
                if x in empty_row:
                    #spath += 1000_000 - 1
                    ni += 999_999 
            sj,ej = min(j, jj), max(j, jj)
            nj = ej
            for y in range(sj,ej+1):
                if y in empty_column:
                    # spath += 1000_000 - 1
                    nj += 999_999
            if ni == ei and nj == ej:
                print('NO DIFF', a, b)
            spath = abs(si - ni) + abs(sj - nj)
            print(a, b, spath)
            total += spath 
print(total)