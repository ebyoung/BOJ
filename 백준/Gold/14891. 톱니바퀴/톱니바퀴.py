from collections import deque


gears = [[]] + [deque(map(int, input())) for _ in range(4)]
K = int(input())

for _ in range(K):
    n, d = map(int, input().split())

    r = 0
    while r < 4 - n:
        if gears[n+r][2] == gears[n+r+1][6]:
            break
        r += 1

    l = 0
    while l < n - 1:
        if gears[n-l][6] == gears[n-l-1][2]:
            break
        l += 1

    nd = d
    for i in range(r+1):
        gears[n+i].rotate(nd)
        nd *= -1

    nd = d * -1
    for i in range(1, l+1):
        gears[n-i].rotate(nd)
        nd *= -1

answer = 0
for i in range(1, 5):
    answer += gears[i][0] * (2 ** (i - 1))

print(answer)
