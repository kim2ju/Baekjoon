import sys

def count5(x):
  temp = x // 5
  result = 0
  while temp != 0:
    result += temp
    temp = temp // 5
  return result

def count2(x):
  temp = x // 2
  result = 0
  while temp != 0:
    result += temp
    temp = temp // 2
  return result
  

input = sys.stdin.readline

n, m = map(int, input().strip().split())

result5 = count5(n)-count5(m)-count5(n-m)
result2 = count2(n)-count2(m)-count2(n-m)

print(min(result5, result2))
