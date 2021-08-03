str=list(map(str,input()))
stack=[]
total=0
tmp=0
for i in str:
    if i=='(' or i=='[':
        stack.append(i)
    elif i==')':
        tmp=0
        while True:
            if len(stack)==0:
                break
            top=stack.pop()
            if top=='(':
                if tmp==0:
                    stack.append(2)
                else:
                    stack.append(2*tmp)
                break
            elif top=='[':
                print(0)
                exit(0)
            else:
                tmp=tmp+int(top)
    elif i==']':
        tmp=0
        while True:
            if len(stack)==0:
                break
            top=stack.pop()
            if top=='[':
                if tmp==0:
                    stack.append(3)
                else:
                    stack.append(3*tmp)
                break
            elif top=='(':
                print(0)
                exit()
            else:
                tmp=tmp+int(top)

for i in stack:
    if i=='(' or i=='[':
        print(0)
        exit()
    else:
        total+=i

print(total)