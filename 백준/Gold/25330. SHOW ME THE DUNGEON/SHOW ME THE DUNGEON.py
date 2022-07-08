def smtd(visited, hp, acc):
    global answer

    flag = True

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            acc += A[i]
            if hp >= acc:
                flag = False
                smtd(visited, hp-acc, acc)
            acc -= A[i]
            visited[i] = 0

    if flag:
        total = 0
        for i in range(N):
            if visited[i]:
                total += P[i]
        answer = max(answer, total)


N, K = map(int, input().split())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
visited = [0] * N
answer = 0
smtd(visited, K, 0)
print(answer)