def change_switch(switches, gender, num):
    if gender == 1:                                 # 남학생이면
        for j in range(num, num_switches + 1, num): # 받은 번호의 배수 번호들을
            switches[j] = 1 - switches[j]   # 반대로 바꾸기

    elif gender == 2:                               # 여학생이면
        switches[num] = 1 - switches[num]   # 받은 번호는 일단 바꾸고
        k = 1                                       # 1칸부터 시작해서
        # 왼쪽과 오른쪽 경계를 넘어가지 않도록 범위 설정, 기준 번호에서 왼쪽으로 k번째와 오른쪽으로 k번째가 같다면
        while k < min(num, num_switches - num + 1) and switches[num - k] == switches[num + k]:
            # 왼쪽 k번째와 오른쪽 k번째를 바꾸기
            switches[num - k] = 1 - switches[num - k]
            switches[num + k] = 1 - switches[num + k]
            k += 1

    return switches

# 입력 받기
num_switches = int(input())
switches = [0] + list(map(int, input().split()))
num_students = int(input())
# 성별과 번호 입력을 받아서 정의한 함수를 이용해 처리
for _ in range(num_students):
    gender, num = map(int, input().split())
    switches = change_switch(switches, gender, num)

# 첫 칸 제외하고 한줄에 20개씩 출력
switches = switches[1:]
for i in range(num_switches//20 + 1):
    print(*switches[(i*20):(i+1)*20])
