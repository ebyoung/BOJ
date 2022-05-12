def dfs(s):
    stack = [(s, 0)]
    while stack:
        v = stack.pop()
        if v[1] == (C-1):
            return 1
        visited[v[0]][v[1]] = 1
        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < R and 0 <= nx < C:
                if not visited[ny][nx] and array[ny][nx] == '.':
                    stack.append((ny, nx))
    return 0


R, C = map(int, input().split())
array = [list(input()) for _ in range(R)]
dxy = [(1, 1), (0, 1), (-1, 1)]
visited = [[0] * C for _ in range(R)]
answer = 0
for i in range(R):
    answer += dfs(i)

print(answer)