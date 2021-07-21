array=[]
sum=0
for i in range(0,9):
    n=int(input())
    array.append(n)
    sum=sum+n
for i in range(0,8):
    for j in range(i+1,9):
        if sum-(array[i]+array[j])==100:
            array[i]=-1
            array[j]=-1
            break
    if array[i]==-1:
        break
array.sort()
array.remove(-1)
array.remove(-1)
for i in array:
    print(i)