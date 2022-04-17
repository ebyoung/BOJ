from collections import deque
from copy import deepcopy


def bfs(start, new_array):
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if new_array[v[0]][v[1]] == 2:
            return visited[v[0]][v[1]] - 1
        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = visited[v[0]][v[1]] + 1
                queue.append((ny, nx))


def select(idx, ch_list):
    global answer
    if len(ch_list) != M:
        if idx < len(chickens):
            ch_list.append(chickens[idx])
            select(idx+1, ch_list)
            ch_list.pop()
            select(idx+1, ch_list)
        return
    new_array = deepcopy(array)
    for ch_y, ch_x in chickens:
        if (ch_y, ch_x) not in ch_list:
            new_array[ch_y][ch_x] = 0
    total = 0
    for house in houses:
        total += bfs(house, new_array)
        if total > answer:
            break
    else:
        answer = total


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            houses.append((i, j))
        elif array[i][j] == 2:
            chickens.append((i, j))
answer = N**4
select(0, [])
print(answer)
