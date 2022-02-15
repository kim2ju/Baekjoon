import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
use = [0] * N
sequence = []

def dfs():
  if len(sequence) == M:
    print(' '.join(map(str, sequence)))
    return

  for i in range(0, N):
    if use[i] == 0:
      sequence.append(num[i])
      use[i] = 1
      dfs()
      use[num.index(sequence.pop())] = 0


dfs()
