def select(idx, sumd):
    global answer
    if sumd > R:
        return
    elif idx == N:
        if sumd >= L:
            mind = 1000000
            maxd = 0
            for d in result:
                mind = min(d, mind)
                maxd = max(d, maxd)
            if maxd - mind >= X:
                answer += 1
        return

    result.append(data[idx])
    select(idx+1, sumd+data[idx])
    result.pop()
    select(idx+1, sumd)


N, L, R, X = map(int, input().split())
data = list(map(int, input().split()))
result = []
answer = 0
select(0, 0)
print(answer)