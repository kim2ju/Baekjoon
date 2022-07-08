import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().strip().split()))
stack = []
result = ['-1'] * N

NGF = {}
for num in num_list:
  if num in NGF:
    NGF[num] += 1
  else:
    NGF[num] = 1

for i in range(0, N):
  while len(stack) != 0 and NGF[num_list[stack[-1]]] < NGF[num_list[i]]:
    result[stack.pop()] = str(num_list[i])
  stack.append(i)

print(" ".join(result))
