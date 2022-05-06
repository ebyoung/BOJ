from copy import deepcopy


def move(d, array, cnt):
    global answer
    if cnt == 5:
        answer = max(answer, max(map(max, array)))
        return

    new_array = deepcopy(array)
    visited = [[0] * N for _ in range(N)]
    move_d = [range(N), range(N)]
    for i in range(2):
        if d[i] > 0:
            move_d[i] = range(N-1, -1, -1)

    for i in move_d[0]:
        for j in move_d[1]:
            cy = i
            cx = j
            ny = cy + d[0]
            nx = cx + d[1]
            while 0 <= ny < N and 0 <= nx < N:
                if new_array[ny][nx] == 0:
                    new_array[ny][nx] = new_array[cy][cx]
                    new_array[cy][cx] = 0
                    cy = ny
                    cx = nx
                    ny += d[0]
                    nx += d[1]
                else:
                    if new_array[ny][nx] == new_array[cy][cx] and not visited[ny][nx]:
                        new_array[ny][nx] += new_array[cy][cx]
                        new_array[cy][cx] = 0
                        visited[ny][nx] = 1
                    break

    for d in dxy:
        move(d, new_array, cnt+1)


N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0
for d in dxy:
    move(d, array, 0)
print(answer)