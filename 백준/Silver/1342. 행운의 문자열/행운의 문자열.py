def make_string(s, visited):
    global count

    if len(s) == N:
        result.add(s)
        return

    for i in range(N):
        if not visited[i]:
            if s == '' or s[-1] != S[i]:
                visited[i] = 1
                make_string(s + S[i], visited)
                visited[i] = 0


S = input()
N = len(S)
visited = [0] * N
result = set()
make_string('', visited)
print(len(result))