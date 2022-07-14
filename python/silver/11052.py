import sys

input = sys.stdin.readline

N = int(input())
price = list(map(int, input().strip().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
  dp[i] = price[i-1]
  for j in range(0, i // 2 + 1):
    dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[N])
