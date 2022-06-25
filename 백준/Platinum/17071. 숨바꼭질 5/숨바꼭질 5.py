from collections import deque


N, K = map(int, input().split())
if N == K:
    print(0)
else:
    answer = 0
    dist = [[0, 0] for _ in range(500001)]
    queue = deque([(N, 1)])
    dist[N][1] = 1
    while queue and not answer:
        v, idx = queue.popleft()
        time = dist[v][idx] + 1
        idx = 1 - idx
        bro = K + (time * (time - 1)) // 2

        if bro > 500000:
            continue

        if dist[bro][idx]:
            answer = time
            break

        for w in [v + 1, v - 1, v * 2]:
            if 0 <= w <= 500000:
                if w == bro:
                    if answer == 0 or time < answer:
                        answer = time
                        break
                if not dist[w][idx]:
                    dist[w][idx] = time
                    queue.append((w, idx))
    print(answer - 1)