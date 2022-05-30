import heapq


N = int(input())
array = [list(map(int, input())) for _ in range(N)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[0] * N for _ in range(N)]
heap = [(0, 0, 0)]
while heap:
    c, cy, cx = heapq.heappop(heap)
    if (cy, cx) == (N-1, N-1):
        print(c)
        break
    for dy, dx in dxy:
        ny = cy + dy
        nx = cx + dx
        if 0 <= ny < N and 0 <= nx < N:
            if not visited[ny][nx]:
                visited[ny][nx] = 1
                if array[ny][nx]:
                    heapq.heappush(heap, (c, ny, nx))
                else:
                    heapq.heappush(heap, (c+1, ny, nx))