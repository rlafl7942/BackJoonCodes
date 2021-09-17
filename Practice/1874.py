## 다시 풀어보기
operation=[]
stack=[]
count=1
flag=0
n=int(input())
for i in range(n):
    num=int(input())
    while True:
        if count>num:
            break
        stack.append(count)
        count+=1
        operation.append('+')
    if stack[-1]==num:
        stack.pop()
        operation.append('-')
    else:
        flag=1
if flag==1:
    print('NO')
else:
    for i in operation:
        print(i)