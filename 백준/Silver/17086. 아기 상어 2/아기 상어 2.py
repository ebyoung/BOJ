from collections import deque


def bfs(s):
    visited = [[0] * M for _ in range(N)]
    visited[s[0]][s[1]] = 1
    queue = deque([s])
    while queue:
        v = queue.popleft()
        if array[v[0]][v[1]]:
            return visited[v[0]][v[1]]

        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = visited[v[0]][v[1]] + 1
                queue.append((ny, nx))


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
dxy = [(dy, dx) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if dy or dx]
max_dist = 0
for i in range(N):
    for j in range(M):
        cur_dist = bfs((i, j))
        if cur_dist > max_dist:
            max_dist = cur_dist

print(max_dist-1)