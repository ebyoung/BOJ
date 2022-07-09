N = int(input())
data = list(map(int, input().split()))
answer = 0
for i in range(N):
    if data[i] <= 1:
        continue

    k = 2
    while k <= (data[i] // 2):
        if not data[i] % k:
            break
        k += 1
    else:
        answer += 1
print(answer)