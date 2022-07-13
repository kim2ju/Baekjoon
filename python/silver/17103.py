import sys

input = sys.stdin.readline

prime = [False, False, True] + [True, False] * 499999

for i in range(3, 1001, 2):
  if prime[i]:
    for j in range(i * i, 1000001, i):
      prime[j] = False

T = int(input())

for i in range(T):
  n = int(input())
  result = 0
  for i in range(2, n//2+1):
    if prime[i]:
      if prime[n-i]:
        result += 1
  print(result)
  
