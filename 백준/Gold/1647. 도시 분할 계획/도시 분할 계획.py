def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    parents[find(y)] = find(x)


N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parents = list(range(N+1))
idx = edge_count = answer = 0
while edge_count < (N - 2):
    s, e, c = edges[idx]
    if find(s) != find(e):
        union(s, e)
        edge_count += 1
        answer += c
    idx += 1
print(answer)