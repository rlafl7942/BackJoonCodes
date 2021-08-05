n=int(input())
score=[]
cnt=0
sum=0
for i in range(0,n):
    quiz=str(input())
    cnt=0
    sum=0
    for j in quiz:
        if j=='O':
            cnt+=1
        else:
            cnt=0
        tmp=j
        sum+=cnt
    score.append(sum)
for i in score:
    print(i)