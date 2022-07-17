import sys

input = sys.stdin.readline

n = int(input())
dp = [[0] * i for i in range(1, n+1)]
dp[0][0] = int(input())

for i in range(2, n+1):
  int_list = list(map(int, input().strip().split()))

  dp[i-1][0] = dp[i-2][0] + int_list[0]
  dp[i-1][i-1] = dp[i-2][i-2] + int_list[i-1]
  for j in range(1, i-1):
    dp[i-1][j] = max(dp[i-2][j-1], dp[i-2][j]) + int_list[j]
  
print(max(dp[n-1]))      
