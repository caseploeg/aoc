#!/usr/bin/env python3


import sys
from collections import Counter


strength = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def get_type(hand):
    s = hand[0]
    counter = Counter(hand)
    m1, m2 = 0, 0  
    for k,v in counter.items():
        if k == 'J':
            continue
        if v >= m1:
            m2 = m1
            m1 = v
        elif v >= m2:
            m2 = v
    if m1 + counter['J']== 5:
        return '5k'
    elif m1 + counter['J'] == 4:
        return '4k'
    elif m1 <= 3 and m2 <= 2 and m1 + m2 + counter['J'] == 5:
        return 'full'
    elif m1 + counter['J'] == 3:
        return '3k'
    elif m1 <= 2 and m2 <= 2 and m1 + m2 + counter['J'] == 4:
        return '2p'
    elif m1 + counter['J'] == 2:
        return '1p'
    else:
        return 'high'

rank = ['5k', '4k', 'full', '3k', '2p', '1p', 'high']

def get_rank(hand):
    return len(rank) - rank.index(get_type(hand))

def get_str(card):
    return len(strength) - strength.index(card)

def cmp(a, b):
    rank_a = get_rank(a[0])
    rank_b = get_rank(b[0])
    if rank_a > rank_b:
        return 1 
    elif rank_b > rank_a:
        return -1
    else:
        for i in range(5):
            c_a = get_str(a[0][i])
            c_b = get_str(b[0][i])
            if c_a - c_b != 0:
                return c_a - c_b
    print("SAME HAND")
    return 0
            
hands = []
for line in sys.stdin:
    hand, bid = line.split()
    bid = int(bid)
    hands.append((hand, bid))

from functools import cmp_to_key, reduce
key_func = cmp_to_key(cmp)
hands = sorted(hands, key=key_func)
print(reduce(lambda x, y: ((hands.index(y)+1) * y[1]) + x, hands, 0))

# print('\n'.join([x[0] + ' ' + str((hands.index(x)+1) * x[1]) for x in hands])) 
