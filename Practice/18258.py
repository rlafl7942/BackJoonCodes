import sys
stack=[]
num=int(input())
for i in range(num):
    order=list(map(str, sys.stdin.readline().split()))
    if order[0]=='push':
        stack.append(order[1])
    elif order[0]=='size':
        print(len(stack))
    elif order[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif len(stack)==0:
        print(-1)
    else:
        if order[0]=='pop':
            print(stack.pop(0))
        elif order[0]=='front':
            print(stack[0])
        elif order[0]=='back':
            print(stack[-1])