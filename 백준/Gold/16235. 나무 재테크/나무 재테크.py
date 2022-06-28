from collections import deque


def adjust(tree):
    x, y, a = tree.split()
    return [int(x)-1, int(y)-1, int(a)]


def ss(trees):
    dead = []
    # 봄: 나이만큼 양분-, 나이 += 1, 어린 나무부터, 양분 부족하면 죽음
    for i in range(N):
        for j in range(N):
            surv = deque()
            while trees[i][j]:
                a = trees[i][j].popleft()
                if land[i][j] >= a:
                    land[i][j] -= a
                    surv.append(a + 1)
                else:
                    dead.append([i, j, a])

                if land[i][j] == 0:
                    break

            while trees[i][j]:
                a = trees[i][j].popleft()
                dead.append([i, j, a])

            trees[i][j] = surv
    # 여름: 죽은 나무 나이 // 2 양분
    for x, y, a in dead:
        land[x][y] += a // 2
    return trees


def fw(trees):
    # 가을: 나이 5의 배수이면 번식, 인접한 8칸에 나이1 나무
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if not trees[i][j][k] % 5:
                    for d in dxy:
                        nx = i + d[0]
                        ny = j + d[1]
                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].appendleft(1)
    # 겨울: 양분 += array[i][j]
    for i in range(N):
        for j in range(N):
            land[i][j] += array[i][j]
    return trees


N, M, K = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, a = adjust(input())
    trees[x][y].append(a)

for i in range(N):
    for j in range(N):
        trees[i][j].sort()
        trees[i][j] = deque(trees[i][j])

land = [[5] * N for _ in range(N)]
dxy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for _ in range(K):
    trees = ss(trees)
    trees = fw(trees)

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])
print(answer)