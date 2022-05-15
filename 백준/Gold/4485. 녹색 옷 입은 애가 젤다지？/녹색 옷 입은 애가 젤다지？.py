import heapq
t = 0
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N = int(input())
while N:
    t += 1
    array = [list(map(int, input().split())) for _ in range(N)]
    visited = [[int(1e9)] * N for _ in range(N)]
    heap = [(array[0][0], 0, 0)]
    while heap:
        c, y, x = heapq.heappop(heap)
        if y == x == (N-1):
            answer = c
            break
        for dy, dx in dxy:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N:
                nc = c + array[ny][nx]
                if visited[ny][nx] > nc:
                    visited[ny][nx] = nc
                    heapq.heappush(heap, (nc, ny, nx))

    print(f'Problem {t}: {answer}')
    N = int(input())