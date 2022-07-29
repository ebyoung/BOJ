def dfs(sy, sx):
    stack = [(sy, sx)]
    cnt = 0
    while stack:
        cy, cx = stack.pop()
        if not array[cy][cx]:
            cnt += 1
            array[cy][cx] = 1
            for dy, dx in dxy:
                ny = cy + dy
                nx = cx + dx
                if 0 <= ny < N and 0 <= nx < M and not array[ny][nx]:
                    stack.append((ny, nx))
    return cnt


N, M, K = map(int, input().split())
array = [[0] * M for _ in range(N)]

for _ in range(K):
    lbx, lby, rtx, rty = map(int, input().split())
    for i in range(lby, rty):
        for j in range(lbx, rtx):
            array[i][j] = 1

results = []
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(N):
    for j in range(M):
        if not array[i][j]:
            cnt = dfs(i, j)
            results.append(cnt)

results.sort()
print(len(results))
print(*results)
