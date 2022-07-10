from collections import deque


def bfs(*args, find=False):
    if find:
        sy, sx = args
    else:
        sy, sx, ey, ex = args

    visited = [[0] * (N + 1) for _ in range(N + 1)]
    visited[sy][sx] = 1
    queue = deque([(sy, sx)])
    results = []
    while queue:
        cy, cx = queue.popleft()

        if find:
            if array[cy][cx] > 1:
                if not results:
                    results.append((cy, cx))
                else:
                    if visited[cy][cx] == visited[results[0][0]][results[0][1]]:
                        results.append((cy, cx))
                    else:
                        results.sort()
                        return visited[results[0][0]][results[0][1]] - 1, array[results[0][0]][results[0][1]] - 2
        else:
            if cy == ey and cx == ex:
                array[sy][sx] = 0
                return visited[cy][cx] - 1, 0

        for dy, dx in dxy:
            ny = cy + dy
            nx = cx + dx
            if 0 < ny <= N and 0 < nx <= N and not visited[ny][nx] and array[ny][nx] != 1:
                visited[ny][nx] = visited[cy][cx] + 1
                queue.append((ny, nx))
    if results:
        results.sort()
        return visited[results[0][0]][results[0][1]] - 1, array[results[0][0]][results[0][1]] - 2
    return K + 1, 0


N, M, K = map(int, input().split())
array = [[1] * (N + 1)] + [[1] + list(map(int, input().split())) for _ in range(N)]
ty, tx = map(int, input().split())
guests = []
for i in range(M):
    sy, sx, ey, ex = map(int, input().split())
    array[sy][sx] = i + 2
    guests.append((sy, sx, ey, ex))

dxy = [(-1, 0), (0, -1), (0, 1), (1, 0)]

cnt = 0
while cnt < M:
    dist, idx = bfs(ty, tx, find=True)
    if dist < K:
        K -= dist
        ty, tx = guests[idx][2], guests[idx][3]
        nd, ni = bfs(*guests[idx])

        if nd <= K:
            K += nd
        else:
            K = -1
            break
    else:
        K = -1
        break
    cnt += 1

print(K)