import heapq
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(D):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))

    pqueue = [(0, C)]
    dist = [10000000] * (N + 1)

    while pqueue:
        c, v = heapq.heappop(pqueue)
        if dist[v] > c:
            dist[v] = c

            for wc, w in graph[v]:
                if dist[w] > c + wc:
                    heapq.heappush(pqueue, (c + wc, w))

    max_val = 0
    com_cnt = 0

    for d in dist:
        if d != int(10000000):
            com_cnt += 1
            if d > max_val:
                max_val = d

    print(com_cnt, max_val)