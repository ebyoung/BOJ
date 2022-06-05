from collections import deque


T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    data = input()[1:-1]
    if data:
        data = deque(map(int, data.split(',')))
    else:
        data = deque([])
    idx = 1
    for func in p:
        if func == 'R':
            idx *= -1
        elif func == 'D':
            if data:
                if idx == 1:
                    data.popleft()
                else:
                    data.pop()
            else:
                answer = 'error'
                break
    else:
        data = list(data)[::idx]
        answer = '['
        for d in data:
            answer += f'{d},'
        answer = answer.rstrip(',')
        answer += ']'
    print(answer)