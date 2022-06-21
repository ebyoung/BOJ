from collections import deque


S = int(input())
queue = deque([(1, 0, 1)])
max_d = S * 2
dp = [10000] * max_d

while queue:
    cur_d, cur_c, cur_t = queue.popleft()
    if cur_t < dp[cur_d]:
        dp[cur_d] = cur_t

    if cur_d == S:
        print(cur_t - 1)
        break

    for new_d, new_c in [(cur_d, cur_d), (cur_d + cur_c, cur_c), (cur_d - 1, cur_c)]:
        if 0 <= new_d < max_d and cur_t < dp[new_d] + 1:
            queue.append((new_d, new_c, cur_t + 1))