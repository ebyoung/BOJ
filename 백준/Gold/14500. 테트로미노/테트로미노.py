def dfs(c, total, count):
    global answer

    if count == 4:
        answer = max(answer, total)
        return

    visited[c[0]][c[1]] = 1
    for d in dxy:
        ny = c[0] + d[0]
        nx = c[1] + d[1]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            dfs((ny, nx), total+array[ny][nx], count+1)
    visited[c[0]][c[1]] = 0


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[0] * M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        k = array[i][j]
        count = 1
        for d in dxy:
            ny = i + d[0]
            nx = j + d[1]
            if 0 <= ny < N and 0 <= nx < M:
                k += array[ny][nx]
                count += 1

        if count == 4:
            answer = max(answer, k)
        if count == 5:
            for d in dxy:
                ny = i + d[0]
                nx = j + d[1]
                answer = max(answer, k - array[ny][nx])

        dfs((i, j), array[i][j], 1)

print(answer)