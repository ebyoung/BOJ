from collections import deque


N, K = map(int, input().split())
visited = [0] * 100002
visited[N] = 1
queue = deque([N])
while queue:
    v = queue.popleft()
    if v == K:
        break
    for w in [v + 1, v - 1, v * 2]:
        if 0 <= w < 100002 and not visited[w]:
            visited[w] = visited[v] + 1
            queue.append(w)
print(visited[K] - 1)
