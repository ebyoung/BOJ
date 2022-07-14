import heapq
import sys
input = sys.stdin.readline


def union(x, y):
    parents[find(y)] = find(x)


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


while 1:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    pqueue = []
    for _ in range(M):
        x, y, z = map(int, input().split())
        heapq.heappush(pqueue, (z, x, y))


    parents = list(range(N))
    cnt = 0
    answer = 0
    while pqueue:
        z, x, y = heapq.heappop(pqueue)
        if find(x) != find(y):
            union(x, y)
            cnt += 1
        else:
            answer += z

    print(answer)