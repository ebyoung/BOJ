A, B, C = map(int, input().split())
if C > B:
    result = A // (C - B) + 1
    print(result)
else:
    print(-1)