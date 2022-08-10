data = input()
answer = 0
idx = 0
N = len(data)
while idx < N:
    if data[idx] == 'c':
        if idx + 1 < N and (data[idx+1] == '=' or data[idx+1] == '-'):
            idx += 1
    elif data[idx] == 'd':
        if (idx + 2 < N and data[idx+1] == 'z' and data[idx+2] == '='):
            idx += 2
        elif (idx + 1 < N and data[idx+1] == '-'):
            idx += 1
    elif data[idx] == 'l':
        if idx + 1 < N and (data[idx+1] == 'j'):
            idx += 1
    elif data[idx] == 'n':
        if idx + 1 < N and (data[idx+1] == 'j'):
            idx += 1
    elif data[idx] == 's':
        if idx + 1 < N and data[idx+1] == '=':
            idx += 1
    elif data[idx] == 'z':
        if idx + 1 < N and data[idx+1] == '=':
            idx += 1
    idx += 1
    answer += 1

print(answer)
