import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
  n = int(input())
  price_list = []
  price_list.append(list(map(int, input().strip().split())))
  price_list.append(list(map(int, input().strip().split())))
  
  dp = [[0] * 3 for _ in range(n+1)]

  for j in range(1, n+1):
    dp[j][0] = max(dp[j-1][1], dp[j-1][2]) + price_list[0][j-1]
    dp[j][1] = max(dp[j-1][0], dp[j-1][2]) + price_list[1][j-1]
    dp[j][2] = max(dp[j-1][0], dp[j-1][1], dp[j-1][2])

  print(max(dp[n]))
    
