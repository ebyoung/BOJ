def drop(in_array):
    array = [[x for x in line] for line in in_array]
    kill = [1]
    while kill:
        kill = []
        for i in range(7):
            j = 0
            while j < 7:
                if array[i][j]:
                    s = j
                    while j < 7 and array[i][j]:
                        j += 1
                    if j < 7:
                        e = j - 1
                    else:
                        e = 6
                    l = e - s + 1
                    for k in range(l):
                        if array[i][e-k] == l:
                            kill.append((i, e-k))
                else:
                    j += 1

            j = 0
            while j < 7:
                if array[j][i]:
                    s = j
                    while j < 7 and array[j][i]:
                        j += 1
                    if j < 7:
                        e = j - 1
                    else:
                        e = 6
                    l = e - s + 1
                    for k in range(l):
                        if array[e-k][i] == l:
                            kill.append((e-k, i))
                else:
                    j += 1

        for ky, kx in kill:
            array[ky][kx] = 0

        for i in range(5, -1, -1):
            for j in range(7):
                ny = i
                while ny < 6 and array[ny][j] and array[ny+1][j] == 0:
                    array[ny][j], array[ny+1][j] = array[ny+1][j], array[ny][j]
                    ny += 1

    count = 0
    for i in range(7):
        for j in range(7):
            if array[i][j]:
                count += 1
    return count

array = [list(map(int, input().split())) for _ in range(7)]
K = int(input())
mini = 49

for i in range(7):
    y = 6
    while array[y][i]:
        y -= 1
        if y < 0:
            break
    else:
        array[y][i] = K
        mini = min(drop(array), mini)
        array[y][i] = 0

print(mini)