def is_available(num):
    num = str(num)
    for n in num:
        if broken[int(n)]:
            return ''
    return num


N = int(input())
M = int(input())
broken = [0] * 10
results = [abs(N - 100)]

if M:
    data = map(int, input().split())
    for d in data:
        broken[d] = 1

if sum(broken) < 10:
    up = down = N
    count = 0
    while 1:
        result_up = is_available(up)
        result_down = is_available(down)
        if result_up or result_down:
            if result_up:
                results.append(count + len(str(result_up)))
            if result_down:
                results.append(count + len(str(result_down)))
            break
        count += 1
        up += 1
        if down > 0:
            down -= 1

answer = min(results)
print(answer)
