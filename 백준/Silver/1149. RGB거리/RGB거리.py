N = int(input())
dp = [[0] * 3 for _ in range(N)]
dp[0] = list(map(int, input().split()))

for i in range(1, N):
    data = list(map(int, input().split()))
    for j in range(3):
        dp[i][j] = data[j] + min([dp[i-1][k] for k in range(3) if k != j])

print(min(dp[-1]))
