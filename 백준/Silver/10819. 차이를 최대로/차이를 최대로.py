def calc_result(array):
    result = 0
    for i in range(0, N-1):
        result += abs(array[i] - array[i+1])
    return result


def make_perm(idx):
    global answer
    if idx == N:
        answer = max(answer, calc_result(output_array))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            output_array[idx] = input_array[i]
            make_perm(idx+1)
            output_array[idx] = 0
            visited[i] = 0


N = int(input())
input_array = list(map(int, input().split()))
output_array = [0] * N
visited = [0] * N
answer = 0
make_perm(0)
print(answer)
