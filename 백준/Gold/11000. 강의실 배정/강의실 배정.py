import heapq
import sys
input = sys.stdin.readline


N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]
data.sort()
time_queue = [0]
for s, e in data:
    t = heapq.heappop(time_queue)
    heapq.heappush(time_queue, e)
    if t > s:
        heapq.heappush(time_queue, t)

print(len(time_queue))