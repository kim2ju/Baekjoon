import sys

input = sys.stdin.readline

A, B = map(int, input().strip().split())
m = int(input())
A_list = list(map(int, input().strip().split()))
B_list = []
num = 0

for i in range(m):
  num += A_list[m-i-1] * A ** i

if num == 0:
  print(0)
else:
  while num != 0:
    B_list.append(str(num % B))
    num = num // B

  print(" ".join(B_list[::-1]))
  
