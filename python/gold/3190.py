from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
snake = [[0] * N for _ in range(0, N)]
apple = [[0] * N for _ in range(0, N)]
direction = deque()
t = 0

D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d = 0

head = [0, 0]
snake[head[0]][head[1]] = 1

tail = deque()
tail.append([head[0], head[1]])

for i in range(0, K):
  x, y = map(int, input().split())
  apple[x-1][y-1] = 1

L = int(input())

for i in range(0, L):
  direction.append(input().split())

while True:
  t += 1
  head[0] += D[d][0]
  head[1] += D[d][1]

  if head[0] < 0 or head[0] >= N or head[1] < 0 or head[1] >= N:
    print(t)
    break

  if snake[head[0]][head[1]] == 1:
    print(t)
    break

  snake[head[0]][head[1]] = 1
  tail.append([head[0], head[1]])

  if apple[head[0]][head[1]] == 0:
    snake[tail[0][0]][tail[0][1]] = 0
    tail.popleft()
  else: 
    apple[head[0]][head[1]] = 0
  
  if len(direction) != 0:
    if t == int(direction[0][0]):
      if direction[0][1] == 'D':
        d = (d + 1) % 4
      else:
        d = (d - 1) % 4

      direction.popleft()
      
