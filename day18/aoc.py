#!/usr/bin/env python3


import sys

grid = []
path = []
ins = []
for line in sys.stdin: 
    ins.append(line.strip().split(' '))
total = 0 

i, j = 0, 0
points = []
for x, (dirr, n, c) in enumerate(ins):
    d = int(c[2:-2],16)
    """
    d = int(n)
    if dirr == 'R':
        ni, nj = i, j+d 
    if dirr == 'D':
        ni, nj = i+d, j 
    if dirr == 'L': 
        ni, nj = i, j-d 
    if dirr == 'U':
        ni, nj = i-d, j 
    
    points.append((ni,nj))
    i,j = ni,nj
    continue
    """

    direction = c[-2]
    if direction == '0':
        dirr = 'R'
        ni, nj = i, j+d 
    if direction == '1':
        dirr = 'D'
        ni, nj = i+d, j 
    if direction == '2':
        dirr = 'L'
        ni, nj = i, j-d 
    if direction == '3':
        dirr = 'U'
        ni, nj = i-d, j 
    
    points.append((ni,nj))
    i,j = ni,nj
print(points)
total = 0
for i in range(len(points)):
    j = (i + 1) % len(points)
    total += (points[i][1]) * (points[j][0])
    total -= (points[j][1]) * (points[i][0])
    
for i in range(len(points)):
    j = (i + 1) % len(points)
    total += abs(points[i][0] - points[j][1])
    total += abs(points[i][1] - points[j][0])
total = abs(total) // 2
print(total)