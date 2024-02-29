import sys
import math


time = [int(x) for x in sys.stdin.readline().split(":")[1].split()]
dist =  [int(x) for x in sys.stdin.readline().split(":")[1].split()]


total = 1


# s * t >= mind
# t-x * x >= mind
# -x^2 + tx = mind
# t:
# o

# b +- sqrt(a^2 + 4ac) / 2b

for i in range(len(time)):
  ways = 0
  mind = dist[i]
  t = time[i] 
  z1 = (-t - math.sqrt(t*t - 4*mind))/ (-2)
  z2 = (-t + math.sqrt(t*t - 4*mind))/ (-2)
  z1, z2 = sorted([z1,z2])
  print(z1,z2)

