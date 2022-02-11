import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
  reverse = False
  error = False

  p = input().rstrip()
  n = int(input())

  list = input().rstrip()[1:-1].split(',')
  if n == 0:
    list = []

  for j in range(len(p)):
    if p[j] == 'R':
      reverse = not reverse

    else:
      if len(list) == 0:
        print('error')
        error = True
        break
      else:
        if reverse:
          list.pop()
        else:
          list.pop(0)

  if not error:
    if reverse:
      list.reverse()
  
    print('['+','.join(list)+']')
    
