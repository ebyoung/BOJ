from collections import deque


def bfs(sy, sx):
    visited = [[0] * M for _ in range(N)]
    visited[sy][sx] = 1
    queue = deque([(sy, sx)])
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in dxy:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and array[ny][nx] == "L":
                visited[ny][nx] = visited[cy][cx] + 1
                queue.append((ny, nx))
    return max(map(max, visited)) - 1


N, M = map(int, input().split())
array = [list(input()) for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0

for i in range(N):
    for j in range(M):
        if array[i][j] == 'L':
            answer = max(answer, bfs(i, j))
print(answer)
