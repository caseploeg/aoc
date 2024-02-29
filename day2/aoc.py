import sys
from collections import defaultdict

possible = 0

for line in sys.stdin:
  d = defaultdict(int) 
  x = line.split(":")
  print(x[0].split())
  gameid = int(x[0].split()[1])
  games = x[1].split(";")
  for g in games:
    pairs = g.split(",")
    for p in pairs:
      xx = p.strip().split()
      n = int(xx[0])
      c = xx[1]
      if n > d[c]:
        d[c] = n
  power = 1
  for c in d:
    power *= d[c]
  possible += power 

print(possible)


