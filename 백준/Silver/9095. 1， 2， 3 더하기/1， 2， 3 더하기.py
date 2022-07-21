T = int(input())

def make(n):
    if (n >= 0) and not dp[n]:
        dp[n] = make(n - 1) + make(n - 2) + make(n - 3)

    return dp[n]


for _ in range(T):
    N = int(input())
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    print(make(N))