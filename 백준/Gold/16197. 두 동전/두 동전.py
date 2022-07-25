def move_coin(coins, cnt):
    global answer

    if cnt > min(10, answer):
        return
    for dy, dx in dxy:
        nc = []
        idx = 0
        for cy, cx in coins:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < M:
                if array[ny][nx] != '#':
                    nc.append((ny, nx))
                else:
                    nc.append((cy, cx))
        if len(nc) == 2:
            move_coin(nc, cnt+1)
        elif len(nc) == 1:
            answer = min(answer, cnt + 1)
            return


N, M = map(int, input().split())
array = [list(input()) for _ in range(N)]
coins = []
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if array[i][j] == 'o':
            coins.append((i, j))
answer = 11
move_coin(coins, 0)
print(answer if answer < 11 else -1)
