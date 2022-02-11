import sys

input = sys.stdin.readline

N = int(input())
height = []
stack = []
sum = 0

for i in range(N):
  height.append(int(input()))

for i in range(0, N):
  while len(stack) != 0 and stack[-1] <= height[i]:
    stack.pop()

  sum += len(stack)
  stack.append(height[i])

print(sum)
