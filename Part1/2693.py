n=int(input())
max=[]
for i in range(0,n):
    arr = list(map(int, input().split()))
    arr.sort()
    max.append(arr[7])

for i in max:
    print(i)