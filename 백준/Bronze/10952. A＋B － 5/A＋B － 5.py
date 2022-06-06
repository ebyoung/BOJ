while True:
    a, b = tuple(map(int, input().split()))
    
    if (a, b) == (0, 0):
        break

    print(a + b)