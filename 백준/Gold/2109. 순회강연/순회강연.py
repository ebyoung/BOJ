import heapq

n=int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]

array.sort(key=lambda x: (x[1]))
pq=[]
for i in array:
  heapq.heappush(pq, i[0])
  if (len(pq)>i[1]):
    heapq.heappop(pq)

print(sum(pq))