from collections import deque


N, K = map(int, input().split())
visited = [[0, 0] for _ in range(100002)]
visited[N] = [1, 1]
queue = deque([N])
count = 0
min_time = 0
while queue:
    v = queue.popleft()

    for w in [v + 1, v - 1, v * 2]:
        if 0 <= w < 100002:
            if not visited[w][0]:
                visited[w] = [visited[v][0] + 1, 1]
                queue.append(w)
            else:
                if visited[w][0] == visited[v][0] + 1:
                    visited[w][1] += 1
                    queue.append(w)
        if w == K:
            if min_time == 0:
                min_time = visited[v][0]
                count += 1
            elif min_time == visited[v][0]:
                count += 1
print(visited[K][0] - 1)
print(visited[K][1])
