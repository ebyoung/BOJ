import sys
input = sys.stdin.readline


def rotate(oper, array):

    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    cy = oper[0] - oper[2] - 1
    cx = oper[1] - oper[2] - 1
    k = oper[2] * 2
    d = 0
    idx = 0
    new_array = [[x for x in line] for line in array]

    while not(d == 3 and idx == k - 1):
        ny = cy + dxy[d][0]
        nx = cx + dxy[d][1]
        new_array[cy][cx], new_array[ny][nx] = new_array[ny][nx], new_array[cy][cx]

        cy = ny
        cx = nx
        idx += 1

        if idx == k:
            d += 1
            idx = 0
    if oper[2] == 1:
        return new_array
    return rotate((oper[0], oper[1], oper[2]-1), new_array)


def select_oper(array, used, cnt):
    global min_val
    if cnt == K:
        for i in range(0, N):
            min_val = min(min_val, sum(array[i]))
        return

    for i in range(K):
        if not used[i]:
            used[i] = 1
            new_array = rotate(opers[i], array)
            select_oper(new_array, used, cnt+1)
            used[i] = 0


N, M, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
opers = [tuple(map(int, input().split())) for _ in range(K)]
used = [0] * K
min_val = sum(array[0])
select_oper(array, used, 0)
print(min_val)