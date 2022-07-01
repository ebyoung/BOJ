from collections import deque


N, K = map(int, input().split())
dp = [100000] * (K + 1)
coins = list(set(int(input()) for _ in range(N)))
queue = deque()
for coin in coins:
    if coin <= K:
        dp[coin] = 1
        queue.append(coin)

while queue:
    v = queue.popleft()
    for coin in coins:
        nc = v + coin
        if nc <= K and dp[nc] > dp[v] + 1:
            dp[nc] = dp[v] + 1
            queue.append(nc)

if dp[K] != 100000:
    print(dp[K])
else:
    print(-1)