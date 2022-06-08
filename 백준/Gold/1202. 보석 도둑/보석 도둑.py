import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
gems = []
for _ in range(N):
    w, v = map(int, input().split())
    heapq.heappush(gems, (w, v))

bags = []
for _ in range(K):
    bag = int(input())
    heapq.heappush(bags, bag)

answer = 0
capable_gem = []

while bags:
    bag = heapq.heappop(bags)

    while gems and bag >= gems[0][0]:
        w, v = heapq.heappop(gems)
        heapq.heappush(capable_gem, -v)

    if capable_gem:
        answer -= heapq.heappop(capable_gem)
    elif not gems:
        break

print(answer)
