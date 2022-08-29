import heapq


def make_map(N, k):
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(min(y1, y2), max(y1, y2)+1):
            for j in range(min(x1, x2), max(x1, x2)+1):
                array[i][j] = k


def dijkstra(*s):
    pq = [(0, *s)]
    visited = [[0] * 501 for _ in range(501)]
    while pq:
        hp, cy, cx = heapq.heappop(pq)
        if (cy, cx) == (500, 500):
            return hp

        if not visited[cy][cx]:
            visited[cy][cx] = 1
            for dy, dx in dxy:
                ny = cy + dy
                nx = cx + dx
                if 0 <= ny <= 500 and 0 <= nx <= 500 and array[ny][nx] < 2:
                    heapq.heappush(pq, (hp+array[ny][nx], ny, nx))
    return -1

N = int(input())
array = [[0] * 501 for _ in range(501)]
make_map(N, 1)
M = int(input())
make_map(M, 2)
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
print(dijkstra(0, 0))