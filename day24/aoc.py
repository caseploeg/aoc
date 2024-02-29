#!/usr/bin/env python3

import sys
import numpy as np

lines = []
for line in sys.stdin: 
    start, vel = line.strip().split(' @ ')
    start = map(int, start.split(', '))
    vel = map(int, vel.split(', '))
    lines.append((np.array(list(start)),np.array(list(vel))))
    continue
pos = set()
coord = 2
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        v1 = lines[i][1]
        v2 = lines[j][1]
        if v1[coord] == v2[coord]:
            possiblex = set() 
            for k in range(-1000, 1000):
                if k != v1[coord]:
                    if (lines[j][0][coord] - lines[i][0][coord]) % (k - v1[coord]) == 0:
                        possiblex.add(k)
            if len(pos):
                pos = pos.intersection(possiblex)
            else:
                pos = possiblex
print(pos)

RVX, RVY, RVZ = -20, -274, 31

(APX, APY, APZ), (AVX, AVY, AVZ) = lines[0]
(BPX, BPY, BPZ), (BVX, BVY, BVZ) = lines[1]
MA = (AVY-RVY)/(AVX-RVX)
MB = (BVY-RVY)/(BVX-RVX)
CA = APY - (MA*APX)
CB = BPY - (MB*BPX)
XPos = int((CB-CA)/(MA-MB))
YPos = int(MA*XPos + CA)
Time = (XPos - APX)//(AVX-RVX)
ZPos = APZ + (AVZ - RVZ)*Time
print(XPos + YPos + ZPos)


















