def dfs(v, cnt):
    global answer
    if cnt > answer:
        answer = cnt
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for d in dxy:
        ny = v[0] + d[0]
        nx = v[1] + d[1]
        if 0 <= ny < R and 0 <= nx < C:
            num_alpha = ord(array[ny][nx]) - 65
            if not visited[num_alpha]:
                visited[num_alpha] = 1
                dfs((ny, nx), cnt+1)
                visited[num_alpha] = 0


R, C = map(int, input().split())
array = [list(input()) for _ in range(R)]
visited = [0] * 26
visited[ord(array[0][0])-65] = 1
answer = 0
dfs((0, 0), 1)
print(answer)