from collections import deque


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
dxy = [(dy, dx) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if dy or dx]

queue = deque([])
for i in range(N):
    for j in range(M):
        if array[i][j]:
            queue.append((i, j))

max_dist = 0
while queue:
    v = queue.popleft()
    cur_dist = array[v[0]][v[1]]
    if cur_dist > max_dist:
        max_dist = cur_dist

    for d in dxy:
        ny = v[0] + d[0]
        nx = v[1] + d[1]
        if 0 <= ny < N and 0 <= nx < M and not array[ny][nx]:
            array[ny][nx] = cur_dist + 1
            queue.append((ny, nx))

print(max_dist-1)