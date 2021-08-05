maxIndex=-1
max=-1
for i in range(0,9):
    n=int(input())
    if n>max:
        max=n
        maxIndex=i
print(max)
print(maxIndex+1)