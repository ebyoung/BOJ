def dfs(s, color):
    stack = [s]
    while stack:
        v = stack.pop()
        if not visited[v[0]][v[1]]:
            visited[v[0]][v[1]] = 1
            for d in dxy:
                ny = v[0] + d[0]
                nx = v[1] + d[1]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if array[ny][nx] == color:
                        stack.append((ny, nx))


N = int(input())
array = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs((i, j), array[i][j])
            count += 1
print(count, end=' ')

for i in range(N):
    for j in range(N):
        if array[i][j] == 'G':
            array[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs((i, j), array[i][j])
            count += 1
print(count)