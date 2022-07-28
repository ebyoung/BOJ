def make_perm(perm, visited):
    global min_val, max_val

    if len(perm) < m:
        for i in range(m):
            if not visited[i]:
                visited[i] = 1
                make_perm(perm + [opers[i]], visited)
                visited[i] = 0
    else:
        prev = data[0]
        for i in range(1, N):
            prev = calc[perm[i-1]](prev, data[i])
        max_val = max(max_val, prev)
        min_val = min(min_val, prev)


N = int(input())
data = list(map(int, input().split()))
num_opers = list(map(int, input().split()))
opers = []
for i in range(4):
    opers.extend([i] * num_opers[i])

calc = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x // y if x * y >= 0 else -1 * (abs(x) // abs(y))]
min_val = 1000000000
max_val = -1000000000
m = len(opers)
visited = [0] * m
make_perm([], visited)
print(max_val)
print(min_val)
