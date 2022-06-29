from collections import deque


def mane(y, x):
    queue = deque([(y, x)])
    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1
    while queue:
        cy, cx = queue.popleft()
        dist = visited[cy][cx]

        if dist > K:
            break

        for dy, dx in dxy:
            ny = dy + cy
            nx = dx + cx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if array[ny][nx] < 3:
                    array[ny][nx] = 1
                queue.append((ny, nx))
                visited[ny][nx] = dist + 1


N, M, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
s = (0, 0)
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(N):
    for j in range(M):
        if array[i][j] == 3:
            mane(i, j)
        elif array[i][j] == 4:
            s = (i, j)

queue = deque([s])
visited = [[0] * M for _ in range(N)]
visited[s[0]][s[1]] = 1
answer = -1

while queue:
    cy, cx = queue.popleft()
    dist = visited[cy][cx]

    for dy, dx in dxy:
        ny = dy + cy
        nx = dx + cx
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            if array[ny][nx] == 0:
                queue.append((ny, nx))
                visited[ny][nx] = dist + 1
            elif array[ny][nx] == 2:
                answer = dist
                queue = False
                break

print(answer)