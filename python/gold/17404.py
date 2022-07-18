import sys

input = sys.stdin.readline

N = int(input())
price_list = []
dp = [[0] * 3 for _ in range(N)]
min_list = []

for i in range(0, N):
  price_list.append(list(map(int, input().strip().split())))

dp[0] = price_list[0]

for i in range(0, 3):
  dp[1][0] = price_list[1][0] + dp[0][i]
  dp[1][1] = price_list[1][1] + dp[0][i]
  dp[1][2] = price_list[1][2] + dp[0][i]
  dp[1][i] = 2001
  
  for j in range(2, N):
  
    dp[j][0] = price_list[j][0] + min(dp[j-1][1], dp[j-1][2])
    dp[j][1] = price_list[j][1] + min(dp[j-1][0], dp[j-1][2])
    dp[j][2] = price_list[j][2] + min(dp[j-1][0], dp[j-1][1])

  dp[N-1][i] = 1000 * N
  min_list.append(min(dp[N-1]))

print(min(min_list))
