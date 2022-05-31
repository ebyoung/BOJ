import sys
input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N = int(input())
xyzs = [(tuple(map(int, input().split())), i) for i in range(N)]
edges = []
for i in range(3):
    xyzs.sort(key=lambda xyz: xyz[0][i])
    for j in range(1, N):
        edges.append((abs(xyzs[j][0][i] - xyzs[j-1][0][i]), xyzs[j][1], xyzs[j-1][1]))

parents = list(range(N))
cost = 0
edges.sort()
for i in range(len(edges)):
    c, x, y = edges[i]
    if find(x) != find(y):
        union(x, y)
        cost += c

print(cost)