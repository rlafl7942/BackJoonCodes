n=int(input())
avg=0
cnt=0
answer=[]
for i in range(0,n):
    score=list(map(int, input().split()))
    for j in range(1,len(score)):
        avg+=score[j]
    avg=avg/score[0]
    for j in range(1,len(score)):
        if avg<score[j]:
            cnt+=1
    answer.append(cnt/score[0])
    cnt=0
    avg=0
for i in answer:
    tmp=round(i*100,3)
    print('{:.3f}%' .format(tmp))