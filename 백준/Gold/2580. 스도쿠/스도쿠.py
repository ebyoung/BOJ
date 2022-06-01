def sudoku(idx):
    global finished

    if finished:
        return 

    if idx == len(zeros):
        finished = True
        for line in array:
            print(*line)
        return

    i, j = zeros[idx]

    visited = [0] * 10
    for k in range(9):
        visited[array[i][k]] = 1
        visited[array[k][j]] = 1

    ii = i // 3
    jj = j // 3
    for ik in range(ii*3, (ii+1)*3):
        for jk in range(jj*3, (jj+1)*3):
            visited[array[ik][jk]] = 1

    for k in range(1, 10):
        if not visited[k]:
            array[i][j] = k
            sudoku(idx + 1)
            array[i][j] = 0


array = [list(map(int, input().split())) for _ in range(9)]
zeros = []
finished = False
for i in range(9):
    for j in range(9):
        if not array[i][j]:
            zeros.append((i, j))
sudoku(0)