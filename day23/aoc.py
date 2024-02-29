#!/usr/bin/env python3

import sys

grid = []
for line in sys.stdin:
  grid.append(list(line.strip()))

deltas = [(0,1),(1,0),(0,-1),(-1,0)]

node = 0

nodes = []
for i in range(1,len(grid)-1):
  for j in range(1,len(grid[0])-1):
    a = grid[i][j-1] in {'>','<'}
    b = grid[i][j+1] in {'<','>'}
    c = grid[i+1][j] in {'v', '^'}
    d = grid[i-1][j] == {'^', 'v'}
    if a + b + c + d > 1:
      grid[i][j] = 'c'

for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == 'c': 
      nodes.append((i,j))
    elif grid[i][j] not in '.#':
      grid[i][j] = '.'

#print('\n'.join((''.join(x) for x in grid)))
nodes.append((0,1))
nodes.append((len(grid)-1,len(grid[0])-2))

from collections import defaultdict
adj = defaultdict(list)

for s in nodes:
  print('~~~')
  print(s)
  q = [(*s,0)]
  seen = set()
  while q:
    i,j,l = q.pop(0)
    if (i,j) in nodes and (i,j) != s: 
      print(i,j,l)
      adj[s].append(((i,j),l))
      continue
    if grid[i][j] != '.' and (i,j) != s:
      continue
    for di, dj in deltas:
      if i+di < 0 or i+di >=len(grid) or j+dj < 0 or j+dj >= len(grid[0]):
        continue
      if (i+di,j+dj) not in seen and grid[i+di][j+dj] != '#':
        q.append((i+di,j+dj,l+1))
        seen.add((i+di,j+dj))
#exit()

def longest(s, end):
  if s == end:
    return 0
  q = [(s,0,[s])]
  maxpath = 0
  maxpathlen = 0
  while q:
    cur, l, seen = q.pop()
    if cur == end:
      maxpath = max(maxpath, l)
      if maxpath == l:
        maxpathlen = max(len(seen), maxpathlen)
      continue

    for (n,w) in adj[cur]:
      if n not in seen:
        q.append((n,l+w,seen + [n]))
  return maxpath, maxpathlen 

end = (len(grid)-1, len(grid[0])-2)
s = (0,1)
#print(adj)
count = -1
"""
while count != 0:
  count = 0
  ndel = []
  for node in adj:
    if len(adj[node]) == 1: 
      print(node, adj[node])
      ndel.append(node)
      count +=  1
  print(count, len(adj))
"""

print(longest(end,s))
"""
x = 0
for pathlen in range(len(nodes)):
  x = max(longestt(end, s, pathlen, '{s} {end}'),x)
  print(x)

print(x)





# longest from s to t with length 3
#  ==
# max(longest from s to u with length 2 + W(u,t)) for all u where t in adj[u]

"""