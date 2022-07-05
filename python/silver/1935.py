import sys

input = sys.stdin.readline

N = int(input())
char_stack = []
num = []


def get_value(x):
  if str(x).isalpha():
    return num[ord(x)-65]
  else:
    return x


expression = input().strip()

for i in range(0, N):
  value = int(input())
  num.append(value)

for e in expression:
  if e == '+':
    calc = get_value(char_stack.pop()) + get_value(char_stack.pop())
    char_stack.append(calc)

  elif e == '-':
    temp1 = get_value(char_stack.pop())
    temp2 = get_value(char_stack.pop())
    calc = temp2 - temp1
    char_stack.append(calc)

  elif e == '*':
    calc = get_value(char_stack.pop()) * get_value(char_stack.pop())
    char_stack.append(calc)

  elif e == '/':
    temp1 = get_value(char_stack.pop())
    temp2 = get_value(char_stack.pop())
    calc = temp2 / temp1
    char_stack.append(calc)
    
  else:
    char_stack.append(e)

print("{:.2f}".format(char_stack[0]))
