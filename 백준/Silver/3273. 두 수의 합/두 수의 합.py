n = int(input())
data = list(map(int, input().split()))
data.sort()
x = int(input())
count = 0
for i in range(n):
    for j in range(i+1, n):
        result = data[i] + data[j]
        if result == x:
            count += 1
        elif result > x:
            break

print(count)
