T = int(input())


def check(l, r):
    while l < r:
        if string[l] != string[r]:
            return (1, l, r)

        else:
            l += 1
            r -= 1

    return (0, l, r)


for _ in range(T):
    string = input()
    answer = 0
    result = check(0, len(string) - 1)
    if result[0]:
        answer += 1
        k, l, r = result
        k1 = check(l+1, r)[0]
        k2 = check(l, r-1)[0]
        answer += min(k1, k2)

    print(answer)