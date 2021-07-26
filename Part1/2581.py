m=int(input())
n=int(input())
arr=[]
sum=0
flag=0
for i in range(m,n+1):
    flag=0
    if i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        arr.append(i)
        sum=sum+i
arr.sort()
if sum>0:
    print(sum)
    print(arr[0])
else:
    print(-1)
