cnt=0
flag=0
n=int(input())
arr=list(map(int, input().split()))

for i in arr:
    flag=0
    if i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            flag=1
    if flag==0:
        cnt=cnt+1

print(cnt)
