array=[]
for i in range(0,10):
    n=int(input())
    array.append(n)
for i in range(0,len(array)):
    array[i]=array[i]%42
setArray=set(array)
array=list(setArray)
print(len(array))