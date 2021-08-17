#틀렸습니다.
n=int(input())
box=[list(input()) for _ in range(n)]
answer=1

def check():
    global answer
    #좌우 확인
    for i in range(n):
        cnt=1
        for j in range(n-1):
            if box[i][j]==box[i][j+1]:
                cnt+=1
                answer=max(cnt,answer)
            else:
                cnt=1
    #위아래 확인
    for i in range(n):
        cnt=1
        for j in range(n-1):
            if box[j][i]==box[j+1][i]:
                cnt+=1
                answer=max(cnt,answer)
            else:
                cnt=1


#좌우 확인 and swap
for i in range(n):
    for j in range(n-1):
        box[i][j], box[i][j+1]=box[i][j+1],box[i][j]
        check()
        box[i][j], box[i][j+1]=box[i][j+1],box[i][j]
#위아래 확인 and swap
for i in range(n):
    for j in range(n-1):
        box[j][i], box[j+1][i] = box[j+1][i], box[j][i]
        check()
        box[j][i], box[j+1][i] = box[j+1][i], box[j][i]
print(answer)