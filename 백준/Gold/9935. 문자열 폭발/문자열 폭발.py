string = input()
bomb = list(input())
bomb_last = bomb.pop()
stack = []

for char in string:
    if char == bomb_last and len(stack) >= len(bomb):
        for i in range(1, len(bomb) + 1):
            if stack[-i] != bomb[-i]:
                stack.append(char)
                break
        else:
            for _ in range(len(bomb)):
                stack.pop()
    else:
        stack.append(char)


if stack:
    print(''.join(stack))
else:
    print('FRULA')