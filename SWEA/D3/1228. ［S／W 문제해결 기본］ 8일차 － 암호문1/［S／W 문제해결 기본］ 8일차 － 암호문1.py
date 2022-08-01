for t in range(1, 11):

    N = int(input())
    # 숫자 11개
    case = list(map(int, input().split()))
    M = int(input())
    # 명령어 리스트
    hey_list = list(input().split())

    for h in range(len(hey_list)):
        hey = []

        # 다음 I전까지의 숫자만으로 이뤄진 리스트 쪼개진 것
        # 명령어 1
        if hey_list[h] == 'I':
            x = int(hey_list[h+1])
            y = int(hey_list[h+2])

            # 숫자 y개 리스트 hey 만들기
            for i in range(h+3, h+3+y):
                hey.append(int(hey_list[i]))

            # case 리스트에서 x 전, 후를 아예 분리해서 숫자 넣고 다시 붙이자!
            f_list = []
            b_list = []
            res = []

            if x != 1:
                f_list = case[:x]
            else:
                f_list.append(case[0])
            b_list = case[x:]

            case = f_list + hey + b_list

    print(f'#{t}', *case[:10])