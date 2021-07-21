array=[]
sum=0
for i in range(0,9):
    n=int(input())
    array.append(n)
    sum=sum+n
for i in range(0,9):
    for j in range(i+1,9):
        if sum-(array[i]+array[j])==100:
            array[i]=0
            array[j]=0

for i in sorted(array):
    if i>1:
        print(i)