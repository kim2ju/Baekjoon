import sys

input = sys.stdin.readline

N = int(input())
inform = []
rank = [1] * N

for i in range(0, N):
  inform.append(list(map(int, input().split())))

for i in range(0, N):
  for j in range(i+1, N):
    if inform[i][0] > inform[j][0] and inform[i][1] > inform[j][1]:
      rank[j] += 1
    elif inform[i][0] < inform[j][0] and inform[i][1] < inform[j][1]:
      rank[i] += 1
    
print(' '.join(map(str, rank)))
