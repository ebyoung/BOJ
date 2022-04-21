N, M = map(int, input().split())
r, c, d = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
back = [2, 3, 0, 1]
count = 0

while True:
    if not visited[r][c]:
        visited[r][c] = 1
        count += 1
    for _ in range(4):
        if d:
            d -= 1
        else:
            d = 3
        nr = r + dxy[d][0]
        nc = c + dxy[d][1]
        if not array[nr][nc] and not visited[nr][nc]:
            r = nr
            c = nc
            break
    else:
        nr = r + dxy[back[d]][0]
        nc = c + dxy[back[d]][1]
        if array[nr][nc]:
            break
        else:
            r = nr
            c = nc

print(count)