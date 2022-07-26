T = int(input())

for _ in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = data[0][0]
    dp[1][0] = data[1][0]
    if n > 1:
        dp[0][1] = data[0][1] + dp[1][0]
        dp[1][1] = data[1][1] + dp[0][0]
        
        for i in range(2, n):
            for j in range(2):
                dp[j][i] = data[j][i]
                dp[j][i] += max(dp[1-j][i-1], dp[1-j][i-2])

    print(max(dp[0][-1], dp[1][-1]))