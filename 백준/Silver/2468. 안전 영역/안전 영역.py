def dfs(sy, sx):
    stack = [(sy, sx)]
    while stack:
        cy, cx = stack.pop()
        if not visited[cy][cx]:
            visited[cy][cx] = 1
            for dy, dx in dxy:
                ny = cy + dy
                nx = cx + dx
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    stack.append((ny, nx))


N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
dxy = [(1, 0), (0, 1), (0, -1), (-1, 0)]
mv = max([max(line) for line in array])
mc = 0

for k in range(mv):
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if array[i][j] <= k:
                visited[i][j] = 1
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j)
                count += 1
    mc = max(mc, count)

print(mc)
