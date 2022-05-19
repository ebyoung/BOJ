from collections import deque
N, M = map(int, input().split())
array = list(range(101))
for _ in range(N+M):
    s, e = map(int, input().split())
    array[s] = e

queue = deque([1])
visited = [1e9] * 101
visited[1] = 0
while queue:
    v = queue.popleft()

    if v == 100:
        print(visited[v])
        break

    for i in range(1, 7):
        w = v + i
        if 0 < w <= 100:
            w = array[w]
            if visited[w] > visited[v] + 1:
                visited[w] = visited[v] + 1
                queue.append(w)