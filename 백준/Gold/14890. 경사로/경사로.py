def is_path(path):
    visited = [0] * N
    for i in range(1, N):
        if path[i] != path[i - 1]:
            if path[i] - path[i - 1] == -1:
                if N - i < L:
                    return False

                for k in range(L):
                    if path[i] != path[i+k]:
                        return False
                    visited[i+k] = 1
            elif path[i] - path[i - 1] == 1:
                if i < L:
                    return False
                for k in range(L):
                    if path[i-1] != path[i-1-k] or visited[i-1-k]:
                        return False
            else:
                return False
    return True


N, L = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
count = 0
for i in range(N):
    if is_path(array[i]):
        count += 1

for j in range(N):
    path = []
    for i in range(N):
        path.append(array[i][j])

    if is_path(path):
        count += 1

print(count)