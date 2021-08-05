result=1
for i in range(0,3):
    n=int(input())
    result*=n
cnt=[0,0,0,0,0,0,0,0,0,0]
while True:
    if result==0:
        break
    tmp=result
    tmp=tmp%10
    cnt[tmp]+=1
    result=result//10
for i in cnt:
    print(i)