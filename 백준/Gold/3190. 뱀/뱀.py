def move_snake(n, d, head, tail):
    global t
    while n:
        head[0] += dxy[d][0]
        head[1] += dxy[d][1]
        if 0 <= head[0] < N and 0 <= head[1] < N:
            nhead = array[head[0]][head[1]]
            if nhead > 9:
                array[head[0]][head[1]] = d
                n -= 1
                t += 1
                if nhead == 10:
                    cur_tail = array[tail[0]][tail[1]]
                    array[tail[0]][tail[1]] = 10
                    tail[0] += dxy[cur_tail][0]
                    tail[1] += dxy[cur_tail][1]
                continue
        return n
    return 0


N = int(input())
K = int(input())
array = [[10] * N for _ in range(N)]
array[0][0] = 0
head = [0, 0]
tail = [0, 0]
for _ in range(K):
    r, c = map(int, input().split())
    array[r-1][c-1] = 20

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
L = int(input())
turn = {'D': 1, 'L': -1}
d = 0
pX = 0
t = 1
for _ in range(L):
    nX, C = input().split()
    nX = int(nX)
    if move_snake(nX-pX, d, head, tail):
        break
    pX = nX
    nd = d + turn[C]
    if nd < 0:
        d = 3
    elif nd > 3:
        d = 0
    else:
        d = nd
    array[head[0]][head[1]] = d
else:
    move_snake(N*2, d, head, tail)
print(t)