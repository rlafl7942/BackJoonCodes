import sys
stack=[]
n=int(sys.stdin.readline())
order=[sys.stdin.readline().strip() for i in range(n)]
for i in range(n):
    a=order[i].split()
    if a[0]=='push':
        stack.append(a[1])
    elif a[0]=='top':
        if len(stack)!=0:
            print(stack[len(stack)-1])
        else:
            print('-1')
    elif a[0]=='pop':
        if len(stack)!=0:
            print(stack.pop())
        else:
            print('-1')
    elif a[0]=='size':
        print(len(stack))
    elif a[0]=='empty':
        if len(stack)==0:
            print('1')
        else:
            print('0')
