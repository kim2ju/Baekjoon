N = int(input())
P = list(map(int, input().split()))
totalTime = 0

P.sort()

for i in range(0, N):
    totalTime += P[i] * (N - i)

print(totalTime)
