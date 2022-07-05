from collections import deque


def bfs(s, e):
    visited = [[0] * N for _ in range(M)]
    queue = deque([s])
    visited[s[0]][s[1]] = 1
    while queue:
        cy, cx = queue.popleft()

        if (cy, cx) == e:
            return visited[cy][cx] - 1

        for dy, dx in dxy:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < M and 0 <= nx < N and not visited[ny][nx] and array[ny][nx] != '#':
                visited[ny][nx] = visited[cy][cx] + 1
                queue.append((ny, nx))



def take_things(take, idx, time):
    global answer

    flag = False
    for i in range(len(take)-1):
        if not take[i]:
            flag = True
            nt = bfs(things[idx], things[i])
            take[i] = 1
            if time + nt < answer:
                take_things(take, i, time+nt)
            take[i] = 0

    if not flag:
        time += bfs(things[idx], E)
        answer = min(answer, time)


N, M = map(int, input().split())
array = [list(input()) for _ in range(M)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
S = (-1, -1)
E = (-1, -1)
things = []
take = [0]
for i in range(M):
    for j in range(N):
        if array[i][j] == 'S':
            S = (i, j)
        elif array[i][j] == 'E':
            E = (i, j)
        elif array[i][j] == 'X':
            things.append((i, j))
            take.append(0)


things.append(S)
answer = 2500
take[-1] = 1
take_things(take, -1, 0)
print(answer)