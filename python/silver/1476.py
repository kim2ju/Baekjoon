import sys

input = sys.stdin.readline

E, S, M = map(int, input().strip().split())
S %= 28
M %= 19

year = E

while True:
  if year % 28 == S:
    if year % 19 == M:
      print(year)
      
      break

  year += 15
  
