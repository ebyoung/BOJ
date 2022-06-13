N = int(input())
data = list(map(int, input().split()))
stack = [0]
answer = [0] * N
for i in range(1, len(data)):
    while stack:
        g = stack.pop()
        if data[g] > data[i]:
            stack.append(g)
            stack.append(i)
            answer[i] = g + 1
            break
    else:
        stack.append(i)
        answer[i] = 0

print(*answer)