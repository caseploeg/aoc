#!/usr/bin/env python3

import sys, resource
from functools import lru_cache

def count(grid):
    grid = [list(x) for x in grid.split('\n')]
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                total += len(grid)-i
    return total
                
def shift_down(grid):
    grid = [list(x) for x in grid.split('\n')]
    grid = list(reversed(grid))
    grid = '\n'.join([''.join(x) for x in grid])
    grid = shift_up(grid)
    grid = [list(x) for x in grid.split('\n')]
    grid = list(reversed(grid))
    grid = '\n'.join([''.join(x) for x in grid])
    return grid

def shift_east(grid):
    grid = [list(x) for x in grid.split('\n')]
    grid = list(zip(*grid))
    grid = list(reversed(grid))
    grid = '\n'.join([''.join(x) for x in grid])
    grid = shift_up(grid)
    grid = [list(x) for x in grid.split('\n')]
    grid = list(reversed(grid))
    grid = list(zip(*grid))
    grid = '\n'.join([''.join(x) for x in grid])
    return grid


@lru_cache(maxsize=None)
def shift_up(grid):
    grid = [list(x) for x in grid.split('\n')]
    moved = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            row = i
            while row-1 >= 0 and grid[row][j] == 'O' and grid[row-1][j] == '.':
                moved += 1
                grid[row-1][j] = 'O'
                grid[row][j] = '.'
                row -= 1
    grid = '\n'.join([''.join(x) for x in grid])
    if moved > 0:
        shift_up(grid)
    return grid 

def shift_west(grid):
    grid = [list(x) for x in grid.split('\n')]
    grid = list(zip(*grid))
    grid = '\n'.join([''.join(x) for x in grid])
    grid = shift_up(grid)
    grid = [list(x) for x in grid.split('\n')]
    grid = list(zip(*grid))
    grid = '\n'.join([''.join(x) for x in grid])
    return grid


def cycle(grid):
    seen = set()
    first = dict()
    cycles = 0
    new_grid = shift_east(shift_down(shift_west(shift_up(grid))))
    while new_grid not in seen:
        cycles += 1
        seen.add(new_grid)
        first[new_grid] = cycles
        grid = new_grid
        new_grid = shift_east(shift_down(shift_west(shift_up(grid))))
        if cycles % 100 == 0:
            print(cycles)
    cycles += 1 
    cycle_len = cycles - first[new_grid]
    amount = (1_000_000_000 - first[grid]) % cycle_len
    print('amount:', amount, 'cyclelen:', cycle_len)
    for _ in range(amount-1):
        new_grid = shift_east(shift_down(shift_west(shift_up(new_grid))))
        print(count(new_grid))
    return new_grid

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))

grid = '\n'.join(''.join(x) for x in grid)
grid = cycle(grid)
#print(grid)
print(count(grid))