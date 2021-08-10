#틀렸습니다.
n=int(input())
box=[list(map(str,input())) for _ in range(n)]
max=0

def check():
    global max
    #좌우 확인
    for i in range(0,n):
        cnt=1
        for j in range(0,n-1):
            if box[i][j]==box[i][j+1]:
                cnt+=1
        if max<cnt:
            max=cnt
    #위아래 확인
    for i in range(0,n):
        cnt=1
        for j in range(0,n-1):
            if box[j][i]==box[j+1][i]:
                cnt+=1
        if max<cnt:
            max=cnt

#좌우 확인 and swap
for i in range(0,n):
    for j in range(0,n-1):
        if box[i][j]!=box[i][j+1]:
            box[i][j], box[i][j+1]=box[i][j+1],box[i][j]
            check()
            box[i][j], box[i][j+1]=box[i][j+1],box[i][j]
#위아래 확인 and swap
for i in range(0,n):
    for j in range(0,n-1):
        if box[j][i]==box[j+1][i]:
            box[j][i], box[j+1][i] = box[j+1][i], box[j][i]
            check()
            box[j][i], box[j+1][i] = box[j+1][i], box[j][i]
print(max)