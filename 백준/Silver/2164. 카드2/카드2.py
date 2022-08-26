from collections import deque
N = int(input())
cards = deque(range(1, N+1))
idx = 1
while len(cards) > 1:
    if idx % 2:
        cards.popleft()
    else:
        c = cards.popleft()
        cards.append(c)
    idx += 1
print(cards[0])