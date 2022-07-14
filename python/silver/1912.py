import sys

input = sys.stdin.readline

N = int(input())
dp = list(map(int, input().strip().split()))

for i in range(1, N):
  if dp[i-1] > 0:
    dp[i] += dp[i-1]

print(max(dp))
