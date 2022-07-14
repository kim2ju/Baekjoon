import sys

input = sys.stdin.readline

N = int(input())
A_list = list(map(int, input().strip().split()))

dp = [1] * N

for i in range(N):
  for j in range(i):
    if A_list[j] < A_list[i]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
