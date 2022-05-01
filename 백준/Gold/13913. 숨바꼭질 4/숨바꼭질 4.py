from collections import deque
import sys


sys.setrecursionlimit(int(1e6))


def find_path(v, cnt, path):
    if cnt == 1:
        print(*path[::-1])
        return 1

    for w in [v + 1, v - 1, v // 2]:
        if 0 <= w < 100002 and visitied[w] == cnt - 1:
            path.append(w)
            if find_path(w, cnt-1, path):
                return 1
            path.pop()


N, K = map(int, input().split())
visitied = [0] * 100002
visitied[N] = 1

# 가장 빠른 시간 계산
queue = deque([N])
while queue:
    v = queue.popleft()
    if v == K:
        break
    for w in [v + 1, v - 1, v * 2]:
        if 0 <= w < 100002 and not visitied[w]:
            queue.append(w)
            visitied[w] = visitied[v] + 1
print(visitied[K] - 1)
# 가장 빠른 경로 확인
find_path(K, visitied[K], [K])
