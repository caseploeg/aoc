#!/usr/bin/env python3
import sys 

def mirror(row, j):
    d = 1 
    while j + d < len(row) and j - d + 1 > -1: 
        if row[j+d] != row[j-d+1]:
            return False
        d += 1
    return True

def f(grid, ignore):
    save = '\n'.join(''.join(_) for _ in grid)
    #print(save)
    #print()

    for j in range(len(grid[0])-1):
        if all([mirror(grid[i], j) for i in range(len(grid))]):
            if ignore != (j+1, 'row'):
                return j+1, 'row'

    grid = list(zip(*grid))    
    for j in range(len(grid[0])-1):
        if all([mirror(grid[i], j) for i in range(len(grid))]):
            if ignore != (j+1, 'col'):
                grid = [[list(x)] for x in save.split('\n')]    
                return j+1, 'col'
    grid = [[list(x)] for x in save.split('\n')]    
    
    return -1, ''

total = 0
grid = []
for line in sys.stdin:
    line = line.strip()
    if line == '':
        # print('\n'.join([''.join(x) for x in grid]))
        n, direction = f(grid, (-1, ''))
        flag =False
        for i in range(len(grid)):
            if flag:
                break
            for j in range(len(grid[0])):
                if flag:
                    break
                if grid[i][j] == '.':
                    grid[i][j] = '#'
                elif grid[i][j] == '#':
                    grid[i][j] = '.'
                nn, dd = f(grid, (n,direction))
                if grid[i][j] == '.':
                    grid[i][j] = '#'
                elif grid[i][j] == '#':
                    grid[i][j] = '.'
                if nn != -1:
                    print(nn)
                    if dd == 'row':
                        total += nn
                    else:
                        total += nn * 100
                    flag = True
        grid = []
        
    else:
        grid.append(list(line))
    
n, direction = f(grid, (-1, ''))
flag = False
for i in range(len(grid)):
    if flag:
        break
    for j in range(len(grid[0])):
        if flag: 
            break
        if grid[i][j] == '.':
            grid[i][j] = '#'
        elif grid[i][j] == '#':
            grid[i][j] = '.'
        nn, dd = f(grid, (n,direction))
        if grid[i][j] == '.':
            grid[i][j] = '#'
        elif grid[i][j] == '#':
            grid[i][j] = '.'
        if nn != -1:
            print(nn)
            if dd == 'row':
                total += nn
            else:
                total += nn * 100
            flag = True

print(total)