import sys
seeds = []
seedtosoil = []
soiltofert = []
ferttowater = []
watertolight = []
lighttotemp = []
temptohumid = []
humidtoloc = []

from collections import defaultdict
maps = defaultdict(list)
header = ''


lowest = float("infinity")
mapn = 0
for line in sys.stdin:
  line = line.strip()
  if header == '':
    header = mapn 
    if line.startswith("seeds:"):
      seeds = [int(x) for x in line.split(":")[1].split()]
  elif line != '':
    maps[header].append([int(x) for x in line.split()])
  else:
    header = ''
    mapn += 1
print(maps)
print(seeds)


sseeds = []
for i in range(0,len(seeds), 2):
  sseeds.append((seeds[i],seeds[i+1]))
print(sseeds)
print(len(sseeds))

for s in sseeds:
  cur = 1
  ranges = [s]
  while cur < 8:
    newranges =  []
    rangec = ranges.copy()
    while(len(ranges)) > 0:
      ran = ranges.pop() 
      tmp, buf = ran
      flag = False
      for m in maps[cur]:
        ds, ss, r = m 
        if tmp >= ss and tmp < ss + r:
          if tmp+buf <= ss+r:
            newranges.append(((tmp + (ds-ss)),buf))
          else:
            newranges.append(((tmp + (ds-ss)),(ss+r-tmp)))
            print(ss+r,buf-(ss+r-tmp))
            ranges.append((ss+r,buf-(ss+r-tmp)))
          flag = True
          break
      if flag == False:
        newranges.append((tmp,buf))
    print(newranges)
    ranges = newranges
    cur += 1
  for r in ranges:
    lowest = min(r[0], lowest)
print(lowest)

# map range --> range
# range = s + buf
# map = s + buf2 --> d + buf2
