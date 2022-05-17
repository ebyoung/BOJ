def dfs(s):
    stack = [s]
    visited[s[0]][s[1]] = 1
    count = 1
    while stack:
        v = stack.pop()
        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < N and 0 <= nx < N and array[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = 1
                count += 1
                stack.append((ny, nx))
    results.append(count)


N = int(input())
array = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
results = []

for i in range(N):
    for j in range(N):
        if array[i][j] and not visited[i][j]:
            dfs((i, j))

results.sort()
print(len(results))
for r in results:
    print(r)
