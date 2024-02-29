#!/usr/bin/env python3
import sys
import itertools
from collections import defaultdict
from functools import lru_cache

# state: (n,i) -> really small
@lru_cache(maxsize=None)
def count(n, i):
    if i == len(x):
        if len(n) == 0 or len(n) == 1 and n[0] == 0:
            print(''.join(x))
            return 1
        return 0
    
    if x[i] == '#':
        if len(n) > 0 and n[0] != 0:
            nums = list(n)
            nums[0] -= 1 
            return count(tuple(nums), i+1)
        else:
            return 0
    elif x[i] == '.':
        if len(n) > 0 and n[0] == 0:
            nums = list(n)
            nums.pop(0)
            return count(tuple(nums), i+1)
        if  len(n) == 0 or i == 0 or x[i-1] == '.':
            return count(n, i+1)
        else:
            return 0
    else:
        c = 0
        if len(n) > 0 and n[0] == 0:
            x[i] = '.'
            nums = list(n) 
            nums.pop(0)
            c += count(tuple(nums),i+1)
        if i == 0 or x[i-1] == '.' or len(n) == 0:
            x[i] = '.'
            c += count(n, i+1)
        if len(n) > 0 and n[0] != 0:
            x[i] = '#'
            nums = list(n)
            nums[0] -= 1
            c += count(tuple(nums),i+1)
        x[i] = '?'
        return c



total =0
linen =0
for line in sys.stdin:
    cache = dict()
    linen += 1
    x, nums = line.strip().split()
    x = (f'{x}?' * 4) + x
    x = list(x)
    nums = nums.split(',')
    nums = [int(x) for x in nums]
    nums = [int(x) for _ in range(5) for x in nums]
    c = count(tuple(nums),0)
    print(c)
    total += c 
    count.cache_clear()
print(total)
    

    

    
