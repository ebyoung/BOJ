def chess(cy):
    global answer
    if cy == N:
        answer += 1

    for cx in range(N):
        fail = False
        if not row[cx]:
            for d in [(-1, 1), (-1, -1)]:
                ny = cy + d[0]
                nx = cx + d[1]
                while 0 <= ny < N and 0 <= nx < N:
                    if array[ny][nx]:
                        fail = True
                        break
                    ny += d[0]
                    nx += d[1]
                if fail:
                    break
            if not fail:
                array[cy][cx] = 1
                row[cx] = 1
                chess(cy+1)
                array[cy][cx] = 0
                row[cx] = 0


N = int(input())
answer = 0
array = [[0] * N for _ in range(N)]
row = [0] * N
for i in range(N):
    array[0][i] = 1
    row[i] = 1
    chess(1)
    array[0][i] = 0
    row[i] = 0
print(answer)