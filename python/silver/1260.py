from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N + 1)]
dfs_visited = [0] * (N+1)
bfs_visited = [0] * (N+1)

for _ in range(M):
  m, n = map(int, input().split())
  graph[m][n] = 1
  graph[n][m] = 1

def DFS(v):
  dfs_visited[v] = 1
  print(v, end = ' ')
  for i in range(1, N+1):
    if dfs_visited[i]==0 and graph[v][i]==1:
      DFS(i)

def BFS(v):
  q = deque()
  q.append(v)
  bfs_visited[v] = 1
  while q:
    node = q.popleft()
    print(node, end=' ')
    for i in range(1, N+1):
      if bfs_visited[i]==0 and graph[node][i]==1:
        bfs_visited[i] = 1
        q.append(i)

DFS(V)
print()
BFS(V)
