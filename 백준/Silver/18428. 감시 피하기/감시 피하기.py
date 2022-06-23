def teacher(cnt, array, s):
    global answer

    if cnt == 3:
        result = True
        for i in range(N):
            for j in range(N):
                if array[i][j] == 'T':
                    for dy, dx in dxy:
                        ny = i + dy
                        nx = j + dx
                        if 0 <= ny < N and 0 <= nx < N and array[ny][nx] == 'S':
                            result = False
                            break

                        while 0 <= ny < N and 0 <= nx < N and array[ny][nx] == 'X' and result:
                            ny += dy
                            nx += dx
                            if 0 <= ny < N and 0 <= nx < N and array[ny][nx] == 'S':
                                result = False
        if result:
            answer = True
        return

    sy, sx = s
    for i in range(0, N):
        for j in range(0, N):
            if i < sy and j < sx:
                continue
            if array[i][j] == 'X':
                array[i][j] = 'O'
                teacher(cnt+1, array, (i, j))
                array[i][j] = 'X'


N = int(input())
array = [input().split() for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = False
teacher(0, array, (0, 0))
if answer:
    print('YES')
else:
    print('NO')