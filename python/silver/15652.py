import sys

input = sys.stdin.readline

N, M = map(int, input().split())
sequence = []

def dfs(prev_num):
  if len(sequence) == M:
    print(' '.join(map(str, sequence)))
    return

  for i in range(prev_num, N + 1):
    sequence.append(i)
    dfs(i)
    sequence.pop()


dfs(1)
