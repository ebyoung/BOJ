from collections import deque


M, N, H = map(int, input().split())
array = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dxy = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
queue = deque([])
count = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if array[h][n][m] == 1:
                queue.append((h, n, m))
            elif array[h][n][m] == 0:
                count += 1
if count == 0:
    print(0)
else:
    while queue:
        v = queue.popleft()
        for d in dxy:
            nz = v[0] + d[0]
            ny = v[1] + d[1]
            nx = v[2] + d[2]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if array[nz][ny][nx] == 0:
                    array[nz][ny][nx] = array[v[0]][v[1]][v[2]] + 1
                    queue.append((nz, ny, nx))
    answer = 0
    fail = False
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if array[h][n][m] > answer:
                    answer = array[h][n][m]
                if array[h][n][m] == 0:
                    fail = True
                    break
    if fail:
        print(-1)
    else:
        print(answer-1)