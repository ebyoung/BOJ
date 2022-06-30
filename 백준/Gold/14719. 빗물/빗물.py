H, W = map(int, input().split())
data = list(map(int, input().split()))
answer = 0

for h in range(1, H + 1):
    prev_i = 0
    for i in range(1, W):
        if data[i] >= h:
            if data[prev_i] >= h:
                answer += (i - prev_i - 1)
            prev_i = i

print(answer)