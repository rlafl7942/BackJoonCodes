h,w=map(int,input().split())
height=list(map(int, input().split()))
max=0
loc=-1
total=0
tmp=0
for i in range(0,len(height)):
    if max<height[i]:
        max=height[i]
        loc=i
for i in range(0,loc+1):
    if height[i]>tmp:
        tmp=height[i]
    total+=tmp
tmp=0
for i in range(w-1,loc,-1):
    if height[i]>tmp:
        tmp=height[i]
    total+=tmp
total=total-sum(height)
print(total)

