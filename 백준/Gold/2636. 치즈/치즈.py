def dfs(*s):
    stack = [s]
    while stack:
        cy, cx = stack.pop()
        if not visited[cy][cx]:
            visited[cy][cx] = 1
            for dy, dx in dxy:
                ny = cy + dy
                nx = cx + dx
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                    if array[ny][nx]:
                        array[ny][nx] = 0
                        visited[ny][nx] = 1
                    else:
                        stack.append((ny, nx))


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

time = 0
pre_count = 0

while 1:
    count = sum(map(sum, array))
    if not count:
        print(time)
        print(pre_count)
        break
    else:
        pre_count = count
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        if not visited[i][0]:
            dfs(i, 0)
        if not visited[i][M-1]:
            dfs(i, M-1)

    for i in range(M):
        if not visited[0][i]:
            dfs(0, i)
        if not visited[N-1][i]:
            dfs(N-1, i)

    time += 1