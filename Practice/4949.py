import sys
def check(str):
    stack=[]
    for i in str:
        if i=='(' or i=='[':
            stack.append(i)
        if stack:
            if i==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return -1
            elif i==']':
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return -1
        else:
            if i==')' or i==']':
                return -1
    return len(stack)
while True:
    str=sys.stdin.readline()
    if str=='.\n':
        break
    if check(str)==0:
        print('yes')
    else:
        print('no')