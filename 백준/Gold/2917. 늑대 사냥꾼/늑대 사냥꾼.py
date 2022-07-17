from collections import deque
import heapq
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
array = [list(input()) for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dist = [[int(250000)] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if array[i][j] == '+':
            queue = deque([(i, j)])
            dist[i][j] = 0
            while queue:
                cy, cx = queue.popleft()
                for dy, dx in dxy:
                    ny = cy + dy
                    nx = cx + dx
                    if 0 <= ny < N and 0 <= nx < M:
                        if dist[ny][nx] > dist[cy][cx] + 1:
                            dist[ny][nx] = dist[cy][cx] + 1
                            queue.append((ny, nx))
        elif array[i][j] == 'V':
            s = (-1 * dist[i][j], i, j)
        elif array[i][j] == 'J':
            e = (i, j)

pq = [s]
visited = [[0] * M for _ in range(N)]
visited[s[1]][s[2]] = 1
min_dist = dist[s[1]][s[2]]
while pq:
    cd, cy, cx = heapq.heappop(pq)
    cd *= -1
    if min_dist > cd:
        min_dist = cd

    if array[cy][cx] == 'J':
        print(min_dist)
        break

    for dy, dx in dxy:
        ny = cy + dy
        nx = cx + dx
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = 1
            nd = dist[ny][nx]
            heapq.heappush(pq, (-nd, ny, nx))
