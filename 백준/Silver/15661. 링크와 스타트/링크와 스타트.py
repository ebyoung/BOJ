def calc_score(team):
    global answer

    score = [0, 0]
    for i in range(N):
        t = team[i]
        for j in range(N):
            if team[j] == t:
                score[t] += array[i][j]
    answer = min(answer, abs(score[0]-score[1]))


def make_team(team, idx, cnt):
    if idx == N:
        o = False
        z = False
        for i in range(N):
            if team[i] == 0:
                o = True
            elif team[i] == 1:
                z = True
            if o and z:
                break
        if o and z:
            calc_score(team)
        return

    team[idx] = 1
    make_team(team, idx+1, cnt+1)
    team[idx] = 0
    make_team(team, idx+1, cnt)


N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
team = [0] * N
idx = 0
cnt = 0
answer = 100000
make_team(team, idx, cnt)
print(answer)
