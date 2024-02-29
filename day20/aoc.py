#!/usr/bin/env python3

import sys

flow = dict() 
types = dict()
state = dict()
for line in sys.stdin:
    s, rest = line.strip().split(' -> ')
    if s[0] == '%':
        s = s[1:]
        types[s] = '%'
        state[s] = 0
    elif s[0] == '&':
        s = s[1:]
        types[s] = '&'
        state[s] = dict() 
    else:
        types[s] = 'b'
    flow[s] = []
    for dest in rest.split(', '):
        flow[s].append(dest)

for s in flow:
    for dest in flow[s]:
        if dest in types and types[dest] == '&':
            state[dest][s] = 0

def f():
    q = [(0, 'broadcaster', 'button')]
    lowcount = 0
    highcount = 0
    while q:
        pulse, module, last = q.pop(0)
        if pulse == 1:
            highcount += 1
        else:
            lowcount += 1
        if module not in types:
            continue
        t = types[module]
        newpulse = -1
        if t == '%' and pulse == 0:
            if state[module] == 0:
                state[module] = 1
                newpulse = 1
            elif state[module] == 1:
                state[module] = 0
                newpulse = 0
        elif t == '&':
            state[module][last] = pulse 
            flag = True
            for v in state[module].values():
                if v == 0:
                    flag = False 
                
                elif module == 'zh':
                    print(press, state[module])
                
            if flag: 
                newpulse = 0
            else:
                newpulse = 1
        elif t == 'b':
            newpulse = pulse
        if newpulse != -1:
            for dest in flow[module]:
                q.append((newpulse,dest,module))
    return highcount, lowcount

total = 0
hicount, lowcount = 0,0
for press in range(14966299):
    if press % 1_000_000 == 0:
        print(press)

    hi, low = f()
    if hi == -1:
        print('yehaw')
        break
    hicount += hi
    lowcount += low
print(hicount, lowcount, hicount*lowcount)




    
