import sys

input = sys.stdin.readline

n = int(input())
stack = []
result = []
possible = True
push_num = 1

for i in range(n):
  num = int(input())
  while num >= push_num:
    stack.append(push_num)
    result.append('+')
    push_num += 1

  if stack[-1] == num:
    stack.pop()
    result.append('-')

  else:
    possible = False

if possible:
  for j in result:
    print(j)
else:
  print('NO')
  
