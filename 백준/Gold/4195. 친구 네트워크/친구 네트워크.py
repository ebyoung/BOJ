def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    px = find(x)
    py = find((y))
    if px != py:
        parents[py] = px
        num_friends[px] += num_friends[py]


T = int(input())
for _ in range(T):
    F = int(input())
    parents = {}
    num_friends = {}
    for _ in range(F):
        friends = input().split()
        for f in friends:
            if not parents.get(f):
                parents[f] = f
                num_friends[f] = 1
        union(*friends)
        print(num_friends[find(friends[0])])