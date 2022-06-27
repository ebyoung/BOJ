import heapq
import sys
input = sys.stdin.readline


def union(x, y):
    parents[find(x)] = find(y)


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def set_water(x):
    water[x] = 1
    root = find(x)
    for i in range(N):
        if find(i) == root:
            water[i] = 1


N = int(input())
cost = [int(input()) for _ in range(N)]
array = [list(map(int, input().split())) for _ in range(N)]
parents = list(range(N))
water = [0] * N
answer = 0
pqueue = []

for i in range(N):
    heapq.heappush(pqueue, (cost[i], i, i))
    for j in range(i+1, N):
        heapq.heappush(pqueue, (array[i][j], i, j))

while pqueue:
    c, v1, v2 = heapq.heappop(pqueue)

    if v1 != v2:
        if find(v1) != find(v2) and (not water[v1] or not water[v2]):
            union(v1, v2)
            answer += c
            if water[v1]:
                set_water(v2)
            elif water[v2]:
                set_water(v1)
    else:
        if not water[v1]:
            answer += c
            set_water(v1)


print(answer)