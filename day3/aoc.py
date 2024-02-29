import sys


eng = []
for line in sys.stdin:
  eng.append('.' + line.strip() + '.')
eng = ['.'*142] + eng + ['.'*142]

print(eng)
ratio = 0

from collections import defaultdict
g = defaultdict(list)

for i, row in enumerate(eng):
  num = 0
  adjgears = set()
  for j, c in enumerate(row):
    if c.isdigit():
      num *= 10
      num += int(c)
      pos = [(i,j), (i-1,j), (i+1,j), (i,j+1), (i-1,j+1), (i+1,j+1), (i,j-1),(i-1,j-1),(i+1,j-1)]
      for p in pos:
        x, y = p
        a = eng[x][y] == '*' 
        if a:
          adjgears.add((x,y))
    else:
      for gear in adjgears:
        g[gear].append(num)
      adjgears = set()
      num = 0

  for gear in adjgears:
    g[gear].append(num)


for gear in g:
  print(gear, g[gear])
  if len(g[gear]) == 2:
    ratio += g[gear][0] * g[gear][1]
print(ratio)
