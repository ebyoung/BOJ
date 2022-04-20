import math


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    parents[find(y)] = find(x)


N, M = map(int, input().split())
data = [0] + [tuple(map(int, input().split())) for _ in range(N)]
parents = list(range(N+1))
edge_count = 0
for _ in range(M):
    s, e = map(int, input().split())
    if find(s) != find(e):
        union(s, e)
        edge_count += 1

edges = []
for i in range(1, N+1):
    for j in range(i+1, N+1):
        w = math.dist(data[i], data[j])
        edges.append((w, i, j))
edges.sort()
idx = answer = 0
while edge_count < N - 1:
    w, s, e = edges[idx]
    idx += 1
    if find(s) != find(e):
        union(s, e)
        answer += w
        edge_count += 1
print(f'{answer:.2f}')