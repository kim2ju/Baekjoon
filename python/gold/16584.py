import sys

input = sys.stdin.readline

def cal(x):
  s = 0
  for j in range(0, len(x)):
    if x[j] == "1":
      s += 2 ** (len(x) - 1 - j)
  return s


K = int(input().rstrip())
S = input().rstrip()
N = len(S)
n = cal(S)

while K < n:
  for i in range(1, len(S)+1):

    if i == len(S):
      S = S[:1] + S[2:]
      
    elif S[i] == "1":
      S = S[:i] + S[i+1:]
      break

  n = cal(S)

print(N-len(S))
