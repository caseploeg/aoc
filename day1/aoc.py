#!/bin/python3

import sys

r = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def rfix(line):
  found = []
  for i, rr in enumerate(r):
    j = 0
    if rr in line:
      if line.find(rr) >= 0:
        found.append((line.index(rr), i+1))
        found.append((line.rindex(rr), i+1))
  found = sorted(found)
  return found

total = 0
for line in sys.stdin:
  found = rfix(line)
  dig = 0
  d = ''
  found2 = []
  for i, c in enumerate(line):
    if c.isdigit():
      found2.append((i, int(c))) 
  found = sorted(found + found2)
  dig = found[0][1] * 10 + found[-1][1]
  print(line, dig)
  total += dig  

print(total)
