n=int(input())
score=list(map(int, input().split()))
maxScore=max(score)
avg=0
for i in range(0,len(score)):
    score[i]=score[i]/maxScore*100
    avg+=score[i]
print(avg/n)