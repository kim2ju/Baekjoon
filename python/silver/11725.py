from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]
q = deque()
q.append(1)

for _ in range(N - 1):
    m, n = map(int, input().split())
    graph[m].append(n)
    graph[n].append(m)

while q:
  node = q.popleft()
  for i in graph[node]:
    if parent[i] == 0:
      parent[i] = node
      q.append(i)

for i in range(2, N+1):
    print(parent[i])
    
