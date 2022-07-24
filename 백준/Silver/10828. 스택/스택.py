import sys
input = sys.stdin.readline

def stack_function(func, num='0'):
    if func == 'push':
        stack.append(int(num))
    elif func == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif func == 'size':
        print(len(stack))
    elif func == 'empty':
        print(0 if stack else 1)
    elif func == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

N = int(input())
stack = []
for _ in range(N):
    command = input().split()
    stack_function(*command)
