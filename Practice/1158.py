n,k=map(int, input().split())
array=[]
result=[]
tmp=k
for i in range(1,n+1):
    array.append(i)
while True:
    result.append(array[k-1])
    del array[k-1]
    if len(array)==0:
        break
    k=k+tmp-1
    while True:
        if k>len(array):
            k=k-len(array)
        else:
            break
cnt=0
a="<"
for i in result:
    a=a+str(i)
    cnt=cnt+1
    if cnt!=n:
        a=a+', '
a=a+">"
print(a)