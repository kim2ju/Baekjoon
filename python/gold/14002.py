import sys

input = sys.stdin.readline

N = int(input())
A_list = list(map(int, input().strip().split()))

dp = [1] * N
dp_index = [i for i in range(N)]

for i in range(0, N):
  for j in range(i):
    if A_list[j] < A_list[i]:
      if dp[j] + 1 > dp[i]:
        dp_index[i] = j
        dp[i] = dp[j] + 1
      
result = max(dp)
x = dp.index(result)
result_list = []

while dp_index[x] != x:
  result_list.append(str(A_list[x]))
  x = dp_index[x]
result_list.append(str(A_list[x]))

print(result)
print(" ".join(result_list[::-1]))
