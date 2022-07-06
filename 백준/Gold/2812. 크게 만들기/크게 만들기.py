N, K = map(int, input().split())
num = input()
cnt = 0
result = [num[0]]
for i in range(1, N):
    while result and cnt < K and result[-1] < num[i]:
        result.pop()
        cnt += 1
    result.append(num[i])

while result and cnt < K:
    result.pop()
    cnt += 1

answer = int(''.join(result))
print(answer)