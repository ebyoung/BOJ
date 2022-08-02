def lotto(idx, array):
    if len(array) == 6:
        print(*array)
        return
    elif idx == len(data):
        return
    array.append(data[idx])
    lotto(idx+1, array)
    array.pop()
    lotto(idx+1, array)


while True:
    data = list(map(int, input().split()))
    k = data[0]
    if k:
        lotto(1, [])
    else:
        break
    print()