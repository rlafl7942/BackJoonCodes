sum=0
cnt=0
arr=[]
n,k=map(int, input().split())
for i in range(1,1001):
    cnt=0
    while True:
        arr.append(i)
        cnt=cnt+1
        if cnt==i:
            break

for i in range(n-1, k):
    sum=sum+arr[i]
print(sum)
