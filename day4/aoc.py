import sys

total = 0

from collections import defaultdict

copies = defaultdict(int)

row = 0 
for line in sys.stdin:
  row += 1
  copies[row] += 1
  xx = line.split(":")
  print(xx)
  cards = xx[1].split("|")
  winning = [int(x) for x in cards[0].strip().split()]
  mine = [int(x) for x in cards[1].strip().split()]
  win = 0
  for m in mine:
    if m in winning:
      win += 1
  for i in range(win):
    copies[row+i+1] += copies[row]
  print(copies)

for i in range(1,row+1):
  total += copies[i]
  print(total)
print(total)
