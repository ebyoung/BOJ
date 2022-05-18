import heapq
def dijk(s):
    dist = [1e9] * (N + 1)
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        c, v = heapq.heappop(heap)
        for w, nc in graph[v]:
            if dist[w] > dist[v] + nc:
                dist[w] = dist[v] + nc
                heapq.heappush(heap, (dist[w], w))

    return dist


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

start = dijk(1)
from_v1 = dijk(v1)
from_v2 = dijk(v2)
case1 = start[v1] + from_v1[v2] + from_v2[N]
case2 = start[v2] + from_v2[v1] + from_v1[N]
result = min(case1, case2)
if result >= 1e9:
    print(-1)
else:
    print(result)