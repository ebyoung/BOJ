import sys
input = sys.stdin.readline


def dfs(s, visited, cnt):
    global answer

    if cnt == 4:
        answer = 1
        return

    visited[s] = 1
    for w in graph[s]:
        if not visited[w] and not answer:
            dfs(w, visited, cnt+1)
    visited[s] = 0


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
visited = [0] * N
for i in range(N):
    dfs(i, visited, 0)

print(answer)
