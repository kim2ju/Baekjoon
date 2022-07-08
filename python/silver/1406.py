import sys

input = sys.stdin.readline

L_stack = list(input().strip())
R_stack = []
M = int(input())

for i in range(M):
  command = input().strip().split()

  if command[0] == 'L' and len(L_stack) != 0:
    R_stack.append(L_stack.pop())
  elif command[0] == 'D' and len(R_stack) != 0:
    L_stack.append(R_stack.pop())
  elif command[0] == 'B' and len(L_stack) != 0:
    L_stack.pop()
  elif command[0] == 'P':
    L_stack.append(command[1])

R_stack.reverse()
print("".join(L_stack)+ "".join(R_stack))
