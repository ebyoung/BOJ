from collections import deque


def find_target(size, position):
    visited = [[0] * N for _ in range(N)]
    queue = deque([position])
    visited[position[0]][position[1]] = 1
    targets = []
    k = 0
    while queue:
        v = queue.popleft()
        if visited[v[0]][v[1]] > k:
            if targets:
                targets.sort()
                array[targets[0][0]][targets[0][1]] = 0
                return targets[0], k - 1
            else:
                k = visited[v[0]][v[1]]

        if array[v[0]][v[1]] and array[v[0]][v[1]] < size:
            targets.append(v)

        for d in dxy:
            ny = v[0] + d[0]
            nx = v[1] + d[1]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and (array[ny][nx] <= size or array[ny][nx] == 9):
                visited[ny][nx] = visited[v[0]][v[1]] + 1
                queue.append((ny, nx))

    if targets:
        targets.sort()
        array[targets[0][0]][targets[0][1]] = 0
        return targets[0], k - 1
    else:
        return 0


N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
fish_cnt = 0
for i in range(N):
    for j in range(N):
        if array[i][j] == 9:
            position = (i, j)
        elif array[i][j] > 0:
            fish_cnt += 1

size = 2
time_cnt = 0
eat_cnt = 0
while fish_cnt:
    next = find_target(size, position)
    if next:
        position, t = next
    else:
        break
    time_cnt += t
    eat_cnt += 1
    fish_cnt -= 1
    if eat_cnt == size:
        eat_cnt = 0
        size = min(size + 1, 7)
print(time_cnt)