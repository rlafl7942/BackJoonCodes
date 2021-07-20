n, k = map(int, input().split())
if n<k:
    low=n
    high=k
else:
    low=k
    high=n
i=1
while True:
    if low%i==0 and high%i==0:
        min=i
    if i>low:
        break
    i=i+1
print(min, int(min*(low/min)*(high/min)))