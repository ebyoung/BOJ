T = int(input())
for _ in range(T):
    n = int(input())
    parent = [0] + list(map(int, input().split()))
    count = 0
    visited = [0] * (n + 1)
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            v = parent[i]
            cycle = [i]
            while True:
                if not visited[v]:
                    visited[v] = 1
                    cycle.append(v)
                    v = parent[v]
                elif v in cycle:
                    start = cycle.index(v)
                    for j in range(start, len(cycle)):
                        count += 1
                    break
                else:
                    break

    print(n - count)