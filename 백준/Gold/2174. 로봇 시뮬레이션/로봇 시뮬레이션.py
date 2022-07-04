A, B = map(int, input().split())
N, M = map(int, input().split())
robo_pos = [(-1, -1)]
robo_drs = [-1]
answer = 'OK'

direc = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(N):
    x, y, d = input().split()
    robo_pos.append((int(x), int(y)))
    robo_drs.append(direc[d])


for _ in range(M):
    r, c, n = input().split()
    r = int(r)
    n = int(n)
    end = False

    if c == 'L':
        for _ in range(n):
            robo_drs[r] -= 1
            if robo_drs[r] < 0:
                robo_drs[r] = 3

    elif c == 'R':
        for _ in range(n):
            robo_drs[r] += 1
            robo_drs[r] %= 4

    elif c == 'F':
        for _ in range(n):
            nx = robo_pos[r][0] + dxy[robo_drs[r]][0]
            ny = robo_pos[r][1] + dxy[robo_drs[r]][1]

            if 0 < nx <= A and 0 < ny <= B:
                y = 0
                for i in range(N+1):
                    if robo_pos[i] == (nx, ny):
                        y = i
                        break

                if not y:
                    robo_pos[r] = (nx, ny)
                else:
                    answer = f'Robot {r} crashes into robot {y}'
                    end = True
                    break

            else:
                answer = f'Robot {r} crashes into the wall'
                end = True
                break

    if end:
        break

print(answer)