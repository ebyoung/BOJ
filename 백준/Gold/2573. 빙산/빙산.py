N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
year = 0
while 1:
    visited = [[0] * M for _ in range(N)]
    start = -1
    num_ice = 0
    year += 1
    for i in range(N):
        for j in range(M):
            if array[i][j]:
                visited[i][j] = 1
                for d in dxy:
                    ny = i + d[0]
                    nx = j + d[1]
                    if 0 <= ny < N and 0 <= nx < M and not array[ny][nx] and array[i][j] and not visited[ny][nx]:
                        array[i][j] -= 1

                if array[i][j]:
                    num_ice += 1
                    if start == -1:
                        start = (i, j)

    if start != -1:
        visited = [[0] * M for _ in range(N)]
        visited[start[0]][start[1]] = 1
        stack = [start]
        count = 0
        while stack:
            v = stack.pop()
            count += 1
            for d in dxy:
                ny = v[0] + d[0]
                nx = v[1] + d[1]
                if 0 <= ny < N and 0 <= nx < M and array[ny][nx] and not visited[ny][nx]:
                    stack.append((ny, nx))
                    visited[ny][nx] = 1

        if count != num_ice:
            print(year)
            break
    else:
        print(0)
        break