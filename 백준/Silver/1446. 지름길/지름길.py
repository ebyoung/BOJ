N, D = map(int, input().split())
dp = list(range(0, D+1))
data = [tuple(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x: x[1])

for i in range(N):
    s, e, d = data[i]
    if e <= D:
        nd = dp[s] + d
        if dp[e] > nd:
            dp[e] = nd

        for j in range(e, D + 1):
            dp[j] = min(dp[j], dp[j - 1] + 1)

print(dp[D])
