import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().strip().split()))
stack = []
result = ['-1' for _ in range(N)]

for i in range(0, N):
  while len(stack) != 0 and num_list[stack[-1]] < num_list[i]:
    result[stack.pop()] = str(num_list[i])
  stack.append(i)

print(' '.join(result))
  
