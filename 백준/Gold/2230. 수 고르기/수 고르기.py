N, M = map(int, input().split())
data = [int(input()) for _ in range(N)]
data.sort()

answer = 3000000000

for i in range(N):
    k = 1
    while i + k < N and data[i+k] - data[i] < M:
        k += 1
    if i + k < N:
        answer = min(data[i+k] - data[i], answer)

print(answer)
