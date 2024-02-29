#!/usr/bin/env python3

import sys

count = 0
for line in sys.stdin:
    seq = [int(x) for x in line.split()]
    # print(seq)
    seqs =[seq]
    flag = True
    while flag:
        flag = False
        diff = []
        for i in range(len(seq)-1):
            x = seq[i+1]-seq[i]
            diff.append(x)
            if x != 0:
                flag = True 
        seqs.append(diff)
        seq = diff

    next = 0
    for seq in reversed(seqs):
        next = seq[0] - next 
    

    count += next
    print(next)
print(count)