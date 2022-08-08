T = int(input())
for _ in range(T):
    s = input()
    count = 0
    answer = 'NO'
    for char in s:
        if char == '(':
            count += 1
        else:
            if count:
                count -= 1
            else:
                break
    else:
        if not count:
            answer = 'YES'
    print(answer)