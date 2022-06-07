from collections import deque


def move():
    visited[hedgehog[0][0]][hedgehog[0][1]] = 1

    while hedgehog:
        h = hedgehog.popleft()
        for d in dxy:
            hy = h[0] + d[0]
            hx = h[1] + d[1]
            if 0 <= hy < R and 0 <= hx < C:
                time = visited[h[0]][h[1]]
                if array[hy][hx] == '.' and time + 1 < visited[hy][hx]:
                    visited[hy][hx] = time + 1
                    hedgehog.append((hy, hx))
                elif array[hy][hx] == 'D':
                    print(time)
                    return

    print('KAKTUS')


R, C = map(int, input().split())
array = [list(input()) for _ in range(R)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[int(1e4)] * C for _ in range(R)]
water = deque([])

for i in range(R):
    for j in range(C):
        if array[i][j] == 'S':
            hedgehog = deque([(i, j)])
        elif array[i][j] == '*':
            water.append((i, j))
            visited[i][j] = 1

while water:
    w = water.popleft()
    for d in dxy:
        wy = w[0] + d[0]
        wx = w[1] + d[1]
        if 0 <= wy < R and 0 <= wx < C and visited[wy][wx] == int(1e4) and array[wy][wx] == '.':
            visited[wy][wx] = visited[w[0]][w[1]] + 1
            water.append((wy, wx))

move()
