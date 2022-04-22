N = int(input())
data = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
for i in range(1, N):
    for j in range(1, len(data[i])-1):
        data[i][j] += max(data[i-1][j-1], data[i-1][j])

print(max(data[N-1]))