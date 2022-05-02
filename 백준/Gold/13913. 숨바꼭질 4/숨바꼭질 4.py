from collections import deque


N, K = map(int, input().split())
visitied = [0] * 100002
visitied[N] = 1
path = [0] * 100002
path[N] = N

# 가장 빠른 시간 계산
queue = deque([N])
while queue:
    v = queue.popleft()
    if v == K:
        break
    for w in [v + 1, v - 1, v * 2]:
        if 0 <= w < 100002 and not visitied[w]:
            queue.append(w)
            visitied[w] = visitied[v] + 1
            path[w] = v
print(visitied[K] - 1)
# 가장 빠른 경로 확인
shortest_path = [K]
idx = K
while path[idx] != idx:
    idx = path[idx]
    shortest_path.append(idx)
shortest_path.reverse()
print(*shortest_path)