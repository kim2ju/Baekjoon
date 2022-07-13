import sys

input = sys.stdin.readline

prime = [False, False, True] + [True, False] * 499999

for i in range(3, 1001, 2):
  if prime[i]:
    for j in range(i * i, 1000001, i):
      prime[j] = False

n = int(input())

while n != 0:
  for i in range(2, 1000001):
    if prime[i]:
      if prime[n-i]:
        print(n, "=", i, "+", n-i)
        break
  n = int(input())
  
