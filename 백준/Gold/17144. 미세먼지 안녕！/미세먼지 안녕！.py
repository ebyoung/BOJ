def dust():
    new_array = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if array[i][j] > 0:
                new_array[i][j] += array[i][j]
                spread = array[i][j] // 5
                for d in dxy:
                    ny = i + d[0]
                    nx = j + d[1]
                    if 0 <= ny < R and 0 <= nx < C and array[ny][nx] != -1:
                        new_array[ny][nx] += spread
                        new_array[i][j] -= spread
            elif array[i][j] == -1:
                new_array[i][j] = -1

    return new_array


def air():
    count = 0
    for i in range(R):
        if array[i][0] == -1:
            cy = i
            cx = 0
            if count:
                dd = [0, 2, 1, 3]
            else:
                dd = [1, 2, 0, 3]

            dy, dx = dxy[dd[0]]
            ny = cy + dy
            nx = cx + dx
            array[ny][nx] = 0
            cy = ny
            cx = nx

            for d in dd:
                dy, dx = dxy[d]
                ny = cy + dy
                nx = cx + dx
                if count:
                    isy = lambda x: bool(i <= x < R)
                else:
                    isy = lambda x: bool(0 <= x <= i)
                while isy(ny) and 0 <= nx < C:
                    if array[ny][nx] != -1:
                        array[cy][cx], array[ny][nx] = array[ny][nx], array[cy][cx]
                    cy = ny
                    cx = nx
                    ny += dy
                    nx += dx
            count += 1


R, C, T = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(R)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(T):
    array = dust()
    air()

answer = 0
for i in range(R):
    for j in range(C):
        if array[i][j] > 0:
            answer += array[i][j]

print(answer)
