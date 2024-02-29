#!/usr/bin/env python3

import sys

dirmap = {
    'north': (0, 1, {'|': 'north', 'L': 'east', 'J': 'west'}),
    'south': (0, -1, {'|': 'south', '7': 'west', 'F': 'east'}),
    'east': (1, 0, {'-': 'east', 'J': 'south', '7': 'north'}),
    'west': (-1, 0, {'-': 'west', 'L': 'south', 'F': 'north'}),
}
min_y = float('inf')
max_y = 0 

pipes = {
    '|': (1,0),
    '-': (0,1),
    'L': ()
}
grid = []
loopgrid = []
for line in sys.stdin:
    grid.append(list(line.strip()))
    loopgrid.append(list(line.strip()))
sx, sy = 0, 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'S':
            sx, sy = x, y


def f(x, y, direction):
    xd, yd, nextmap = dirmap[direction]
    next = grid[y+yd][x+xd]
    if next == 'S':
        return x+xd, y+yd, ''
    if next in nextmap:
        next_dir = nextmap[next]
        return x+xd, y+yd, next_dir
    else:
        return f'{next} is invalid while dir is {direction}'
updown = 'n'
def bfs():
    x, y, direction = sx, sy, 'north'
    count = 0
    while True:  
        if (x, y) == (sx, sy) and count != 0:
            return count
        if direction == 'north':
            updown = 'n'
        elif direction == 'south':
            updown = 's'
        loopgrid[y][x] = updown 
        x, y, direction = f(x, y, direction)


        count += 1

loop_len = bfs()
print(loop_len // 2 + loop_len % 2)

def bfs2():
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            # depending on the input, either n or s needs to be on the right side
            if loopgrid[y][x] == 'n':
                i = 1
                # walk until we find the other side of the loop (it must exist)
                while loopgrid[y][x+i] not in  {'n','s'}:
                    if loopgrid[y][x+i] != 'x':
                        count += 1
                    loopgrid[y][x+i] = 'x'
                    i+=1
    return count
            

print(bfs2())

