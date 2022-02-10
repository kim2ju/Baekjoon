import sys

input = sys.stdin.readline

N, P = map(int, input().split())
stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
finger_move = 0

def comparison(stack, num):
  temp = 0

  while not(len(stack) == 0 or stack[-1] <= num):
    temp += 1
    stack.pop()

  if len(stack) != 0:
    if stack[-1] != num:
      temp += 1
      stack.append(num)

  else: 
    temp += 1
    stack.append(num) 

  return temp


for i in range(N):
  a, b = map(int, input().split())

  if a == 1:
    finger_move += comparison(stack1, b)

  elif a == 2:
    finger_move += comparison(stack2, b)

  elif a == 3:
    finger_move += comparison(stack3, b)

  elif a == 4:
    finger_move += comparison(stack4, b)

  elif a == 5:
    finger_move += comparison(stack5, b)
  
  else:
    finger_move += comparison(stack6, b)

print(finger_move)
