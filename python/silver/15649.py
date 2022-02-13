import sys

input = sys.stdin.readline

N, M = map(int, input().split())
use = [0] * N
sequence = []

def dfs():
  if len(sequence) == M:
    print(' '.join(map(str, sequence)))
    return

  for i in range(0, N):
    if use[i] == 0:
      sequence.append(i + 1)
      use[i] = 1
      dfs()
      use[sequence.pop() - 1] = 0


dfs()
