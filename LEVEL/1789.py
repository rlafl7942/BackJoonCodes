n=int(input())
for i in range(1,n):
    if (i*(i+1))/2<=n:
        if ((i+1)*(i+2))/2>n:
            break
print(i)