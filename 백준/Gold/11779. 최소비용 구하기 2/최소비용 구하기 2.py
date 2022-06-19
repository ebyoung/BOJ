import heapq
import sys
input = sys.stdin.readline

def find_path(target):
    global count
    count += 1
    if city_from[target] != target:
        find_path(city_from[target])
    else:
        print(count)
    print(target, end=' ')

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))

A, B = map(int, input().split())
pqueue = [(0, A)]
dist = [int(1e9)] * (N + 1)
dist[A] = 0
city_from = [0] * (N + 1)
city_from[A] = A

while pqueue:
    c, e = heapq.heappop(pqueue)
    if e == B:
        break
    for wc, w in graph[e]:
        cost = c + wc
        if cost < dist[w]:
            dist[w] = cost
            city_from[w] = e
            heapq.heappush(pqueue, (cost, w))

print(dist[B])
count = 0
find_path(B)