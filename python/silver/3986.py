import sys

input = sys.stdin.readline

N = int(input())
stack = []
result = 0

for i in range(0, N):
  str_list = input().strip()
  for s in str_list:
    if len(stack) == 0:
      stack.append(s)
    elif stack[-1] == s:
      stack.pop()
    else:
      stack.append(s)
  if len(stack) == 0:
    result += 1
  stack = []

print(result)
