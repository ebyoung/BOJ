import sys
from collections import deque

def dfs(union_xy, union_people):
    stack = union_xy[:]
    while stack:
        v = stack.pop()
        if not visited[v[0]][v[1]]:
            visited[v[0]][v[1]] = 1
            union_xy.append(v)
            union_people += array[v[0]][v[1]]
            for d in dxy:
                ny = v[0] + d[0]
                nx = v[1] + d[1]
                if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                    if L <= abs(array[ny][nx] - array[v[0]][v[1]]) <= R:    # 절댓값 처리를 깜빡
                        stack.append((ny, nx))
    union_people //= len(union_xy)
    return union_xy, union_people


n, L, R = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
is_union = True
day = 0
while is_union:
    is_union = False
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):                      # 국가들을 하나씩 확인
            if not visited[i][j]:               # 확인하지 않은 국가라면
                queue = deque([(i, j)])         # 큐에 넣고
                union_xy = []                   # 연합 국가들을 저장할 리스트
                union_people = 0                # 연합의 인구수를 저장할 변수
                union_count = 0
                # bfs
                while queue:                    # bfs를 돌며
                    v = queue.popleft()
                    if not visited[v[0]][v[1]]:
                        visited[v[0]][v[1]] = 1 # 방문 처리 하고
                        union_xy.append(v)      # 연합 국가 리스트에 추가
                        union_people += array[v[0]][v[1]]   # 인구수 갱신
                        union_count += 1
                        for d in dxy:
                            ny = v[0] + d[0]
                            nx = v[1] + d[1]
                            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                                if L <= abs(array[ny][nx] - array[v[0]][v[1]]) <= R:  # 절댓값 처리를 깜빡
                                    queue.append((ny, nx))
                union_people //= union_count  # 인구수 평균을 계산

                if union_count > 1:
                    is_union = True
                    for xy in union_xy:         # 연합 국가들의 인구 수를 평균값으로 갱신
                        array[xy[0]][xy[1]] = union_people
    if is_union:
        day += 1    # 실수
print(day)
