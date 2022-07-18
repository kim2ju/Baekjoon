import sys

input = sys.stdin.readline

N = int(input())

if N % 2:
  print(0)
else:
  n = N // 2

  dp = [0] * (n+1)
  dp[0] = 1
  dp[1] = 3

  for i in range(2, n+1):
    dp[i] = dp[i-1] * 3 + sum(dp[:i-1]) * 2

  print(dp[n])
