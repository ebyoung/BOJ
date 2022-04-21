T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    print(N-1)