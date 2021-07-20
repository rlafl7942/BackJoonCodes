max=0
sum=0
for i in range(0,10):
    n, k = map(int, input().split())
    sum=sum-n+k
    if max<sum:
        max=sum

print(max)