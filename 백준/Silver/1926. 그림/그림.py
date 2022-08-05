def dfs(sy, sx):
    stack = [(sy, sx)]
    count = 0

    while stack:
        cy, cx = stack.pop()
        if not visited[cy][cx]:
            visited[cy][cx] = 1
            count += 1
            l = array[cy][cx]
            for dy, dx in dxy:
                ny = cy + l * dy
                nx = cx + l * dx
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and array[ny][nx]:
                    stack.append((ny, nx))
    return count


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[0] * M for _ in range(N)]
max_count = 0
n_pict = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and array[i][j]:
            n_pict += 1
            max_count = max(max_count, dfs(i, j))

print(n_pict)
print(max_count)
