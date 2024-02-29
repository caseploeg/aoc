#!/usr/bin/env python3

import sys

def hash(s):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur

line = sys.stdin.readline()
inss = line.strip().split(',')
m = dict()
for ins in inss:
    val = ins[-1]
    if val == '-':
        op = val
        key = ins[:-1]
    else:
        op = ins[-2] 
        key = ins[:-2]

    h = hash(key)
    if h not in m:
        m[h] = [] 
    box = m[h]
    if op == '-' and len(box) > 0:
        for i, b in enumerate(box):
            bk, bv = b
            if key == bk:
                box.pop(i)
                break
    elif op == '=':
        flag = False
        for i, b in enumerate(box):
            bk, bv = b
            if key == bk:
                box[i] = (key, val)
                flag = True
                break
        if not flag:
            box.append((key, val))

total = 0
for i in range(256):
    if i not in m:
        continue
    box = m[i]
    for j in range(len(box)):
        bk, bv = box[j]
        total += int(bv) * (1+j) * (1+i)
print(total)
