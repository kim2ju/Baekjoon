import sys

input = sys.stdin.readline

N = int(input())
dp = [[0] * 2 for _ in range(N)]
dp[0] = [1, 2] #dp[x][0]은 그 줄에 사자가 0마리일 때 경우의 수. dp[x][1]은 사자가 한 마리일 때 경우의 수

for i in range(1, N):
  dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % 9901
  dp[i][1] = (2 * dp[i-1][0] + dp[i-1][1]) % 9901

print(sum(dp[N-1]) % 9901)
