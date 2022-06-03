import heapq


N = int(input())
array = [int(input()) for _ in range(N)]
heapq.heapify(array)
total = 0
while len(array) > 1:
    v1 = heapq.heappop(array)
    v2 = heapq.heappop(array)
    nv = v1 + v2
    total += nv
    heapq.heappush(array, nv)
print(total)