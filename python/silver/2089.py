import sys

input = sys.stdin.readline

N = int(input())
result = ""

if N == 0:
  print(0)
else:
  while N != 0:
    if N % (-2) == -1:
      result = "1" + result
      N = N // (-2) + 1
    else:
      result = "0" + result
      N = N // (-2)
  print(result)
  
