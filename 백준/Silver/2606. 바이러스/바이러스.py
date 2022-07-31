C = int(input())
N = int(input())
graph = [[] for _ in range(C+1)]
for _ in range(N):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

stack = [1]
visited = [0] * (C + 1)
while stack:
    v = stack.pop()
    if not visited[v]:
        visited[v] = 1
        for w in graph[v]:
            if not visited[w]:
                stack.append(w)
print(sum(visited) - 1)