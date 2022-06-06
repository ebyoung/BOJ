N, M, cy, cx, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
data = list(map(int, input().split()))
dxy = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [0] * 7
roll = [1, 4, 3, 5, 2]
oppo = [0, 2, 1, 4, 3]
top = 1

for d in data:
    ny = cy + dxy[d][0]
    nx = cx + dxy[d][1]
    if 0 <= ny < N and 0 <= nx < M:
        roll[oppo[d]] = roll[0]
        roll[0] = roll[d]
        roll[d] = 7-top
        top = roll[0]
        cy = ny
        cx = nx
        if array[cy][cx]:
            dice[7-top] = array[cy][cx]
            array[cy][cx] = 0
        else:
            array[cy][cx] = dice[7-top]
        print(dice[top])
