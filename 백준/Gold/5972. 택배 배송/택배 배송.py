import heapq


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [int(1e9)] * (N + 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

pqueue = [(0, 1)]
dist[1] = 0
while pqueue:
    c, v = heapq.heappop(pqueue)
    if v == N:
        break

    for nc, w in graph[v]:
        if dist[w] > dist[v] + nc:
            dist[w] = dist[v] + nc
            heapq.heappush(pqueue, (dist[w], w))

print(dist[N])
