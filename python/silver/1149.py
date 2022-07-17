import sys

input = sys.stdin.readline

N = int(input())
price_list = []
dp = [[0] * 3 for _ in range(N)]

for i in range(N):
  price_list.append(list(map(int, input().strip().split())))
  
dp[0] = price_list[0]

for j in range(1, N):
  dp[j][0] = price_list[j][0] + min(dp[j-1][1], dp[j-1][2])
  dp[j][1] = price_list[j][1] + min(dp[j-1][0], dp[j-1][2])
  dp[j][2] = price_list[j][2] + min(dp[j-1][0], dp[j-1][1])

print(min(dp[N-1]))
