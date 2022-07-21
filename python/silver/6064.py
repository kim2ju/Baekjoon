import sys

input = sys.stdin.readline


def find_year(M, N, x, y):
  y %= N
  for i in range(x, M*N+1, M):
    if i % N == y:
      return i
  return -1
  

T = int(input())

for i in range(0, T):
  M, N, x, y = map(int, input().strip().split())
  print(find_year(M, N, x, y))
  
