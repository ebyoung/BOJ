import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            value = heapq.heappop(heap)
            print(value[1])
        else:
            print(0)
