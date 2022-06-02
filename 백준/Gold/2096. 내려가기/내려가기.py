N = int(input())
max_prev = [0] * 3
min_prev = [0] * 3
max_dp = [0] * 3
min_dp = [0] * 3

for _ in range(N):
    line = list(map(int, input().split()))
    for i in range(3):
        min_dp[i] = min_prev[i] + line[i]
        for k in [-1, 0, 1]:
            if 0 <= i + k < 3:
                max_dp[i] = max(max_dp[i], max_prev[i+k] + line[i])
                min_dp[i] = min(min_dp[i], min_prev[i+k] + line[i])
    max_prev = max_dp[:]
    min_prev = min_dp[:]

print(max(max_prev), min(min_prev))