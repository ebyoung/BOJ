N, X = map(int, input().split())
answer = []
if 26 * N < X or N > X:
    answer.append('!')
else:
    answer = N * [65]
    X -= N
    for i in range(N-1, -1, -1):
        if X >= 25:
            answer[i] += 25
            X -= 25
        else:
            answer[i] += X
            break
    answer = list(map(chr, answer))
print(''.join(answer))