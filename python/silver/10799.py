import sys

input = sys.stdin.readline

express = input().strip()
num = 0
result = 0

for i in range(len(express)):
  if express[i] == "(":
    if express[i+1] == ")":
      result += num
    else:
      num += 1
      result += 1
  else:
    if express[i-1] != "(":
      num -= 1

print(result)
    
