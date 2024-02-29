#!/usr/bin/env python3

import sys

workflows = dict() 
parts = []
flag = False
ranges = []
for line in sys.stdin:
    line = line.strip()
    if line == '':
        flag = True
        break
    if flag:
        part = line.strip('{}').split(',')
        p = dict()
        for s in part:
            p[s[0]] = int(s[2:])
        parts.append(p)
    else:
        key, v = line.strip('}').split('{')
        workflows[key] = v.split(',')
paths = []

def f(cur, path):
    if cur not in {'A', 'R'}:
        total = 0
        for i, flow in enumerate(workflows[cur]):
            try:
                rest, next = flow.split(':')
                t = f(next, path + f':{i}')
                total += t
            except:
                total += f(flow, path + f':{i}')
                return total
    if cur == 'A':
        t = 1
        print(path)
        paths.append(path)
        return t 
    return 0








total = f('in', 'in')
total = 0
expected = 167409079868000
for p in paths:
    start = {'x':[1,4000], 's':[1,4000], 'a':[1,4000], 'm':[1,4000]}
    steps = p.split(':')
    curflow = workflows['in']
    for i in range(1,len(steps)):
        for j, flow in enumerate(curflow):
            print(j,flow)
            if len(flow.split(':')) > 1:
                rest, next = flow.split(':')
                if j == int(steps[i]):
                    k = rest[0]
                    op = rest[1]

                    val = int(rest[2:])
                    print(steps, p)
                    print(i, steps[i], j, k,op,val)
                    if op == '>':
                        start[k][0] = max(val+1, start[k][0])
                    elif op == '<':
                        start[k][1] = min(val-1, start[k][1])
                    if next == 'A':
                        break
                    curflow = workflows[next]
                    break
                else:
                    k = rest[0]
                    op = rest[1]
                    val = int(rest[2:])
                    if op == '>':
                        start[k][1] = max(val+1, start[k][0])-1
                    elif op == '<':
                        start[k][0] = min(val-1, start[k][1])+1
            elif flow == 'A':
                break
            else:
                curflow=workflows[flow]
                print(flow, 'except!') 
    print('~~~')
    t = 1
    print(p)
    print(start)
    for k,v in start.items():
        t *= (v[1] - v[0] + 1)
    print(t)
    total += t
    print()
print(total)
print(total - expected)


