n=int(input())
info=[]
rank=1
max_h=0
max_w=0
ranking=[]
for i in range(n):
    person=list(map(int, input().split()))
    info.append(person)
for i in info:
    rank=1
    for j in info:
        if i!=j:
            if i[0]<j[0]:
                if i[1]<j[1]:
                    rank+=1
                else:
                    continue
        else:
            continue
    ranking.append(rank)
for i in ranking:
    print(i, end=' ')