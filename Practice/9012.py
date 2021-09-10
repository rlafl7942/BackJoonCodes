import sys
stack=[]
n=int(sys.stdin.readline())
parenthesis=[sys.stdin.readline().strip() for i in range(n)]
for i in range(n):
    stack=[]
    for j in parenthesis[i]:
        if j=='(':
            stack.append(j)
        elif j==')':
            if len(stack)==0:
                stack.append(j)
            elif stack[len(stack)-1]=='(':
                stack.pop()
    if len(stack)==0:
        print('YES')
    else:
        print('NO')